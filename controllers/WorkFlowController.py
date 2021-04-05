import os

from constants import UPLOAD_FOLDER
from controllers.AccountController import AccountController
from controllers.StepController import WorkFlowStepController
from util.fileHelper import FileHelper
from util.transactionHelper import TransactionHelper
from util.validatorHelper import ValidatorHelper
from controllers.UserController import UserController

from managers.WorkFlowManager import WorkFlowManager
from managers.WorkFlowStepManager import WorkFlowStepManager


class WorkFlowController:

    def process_file(self, json_file):
        """
        Reads and saves a json file
        :param json_file: json file uploaded
        """
        if json_file:
            file_helper = FileHelper()
            filename = file_helper.save_file()
            my_file = os.path.join(UPLOAD_FOLDER, filename)
            workflow_data = file_helper.read_file(my_file)
            self.save_workflow(workflow_data)

    def save_workflow(self, workflow_data):
        """
        Saves workflow data
        :param workflow_data: Dict, workflow data. Ie,
            {
                "trigger": {
                    "params": {
                        "user_id": "105398891",
                        "pin": 2090
                    },
                    "transitions": [
                      {
                        "target": "validate_account",
                        "condition": []
                      }
                    ],
                    "id": "start"
                },
                ....
            }
        """
        workflow_id = WorkFlowManager().insert_one(workflow_data.get("trigger"))
        steps = workflow_data.get('steps')
        for step in steps:
            step["workflow_id"] = workflow_id
        WorkFlowStepManager().insert_many(steps)
        self.start_workflow(workflow_id)

    def start_workflow(self, workflow_id):
        """
        Starts workflow process
        :param workflow_id: str, workflow id. Ie, 606a27bd7b047751c312768e
        """
        workflow = WorkFlowManager().findById(workflow_id)
        trigger = workflow.get("trigger")
        params = {trigger.get('id'): trigger.get('params')}
        self.process_steps(workflow_id, trigger, params)

    def process_steps(self, workflow_id, step, result):
        """
        Process each workflow step
        :param workflow_id: str, workflow id. Ie, 606a27bd7b047751c312768e
        :param step: Dict, step to process. Ie,
            {
              "id": "account_balance_200",
              "params": {
                "user_id": {"from_id": "start", "param_id": "user_id"}
              },
              "action": "get_account_balance",
              "transitions": [
                {
                  "condition": [
                    {"from_id": "account_balance", "field_id": "balance", "operator": "gt", "value": 250000}
                  ],
                  "target": "withdraw_50"
                }
              ]
            }
        :param result: Dict, contains params data can be entries for post steps. Ie,
            {
                'start': {'user_id': '105398891', 'pin': 2090},
                'validate_account': {'is_valid': True},
                'account_balance': {'balance': 294700.0},
                ...
            }

        """
        print("\nprocess step: {}".format(step.get("id")))
        print(result)
        transitions = step.get('transitions')
        print(transitions)
        for transition in transitions:
            next_step = None
            if self.validate_condition(transition.get('condition', []), result):
                next_step = WorkFlowStepController().get_workflow_step(
                    workflow_id=workflow_id,
                    step_id=transition.get('target'))
            if next_step:
                step_parameters = self.get_result_field(next_step.get('params'), result)
                method_to_call = getattr(self, next_step.get('action'))
                response = method_to_call(**step_parameters)
                if response:
                    result.update(response)
                self.process_steps(workflow_id, next_step, result)

    @staticmethod
    def validate_account(user_id, pin):
        """
        Validates an account
        :param user_id: str, user id. Ie, '105398891'
        :param pin: Int, pin. Ie, 2090
        :return: Dict, response. Ie, {"is_valid": False}
        """
        response = {"validate_account": {"is_valid": False}}
        if user_id and pin:
            UserController().create_new_user(user_id, pin)
            response["validate_account"]["is_valid"] = True
        return response

    @staticmethod
    def withdraw_in_dollars(user_id, money):
        """
        withdraw from the account in dollars
        :param user_id: str, user id. Ie, '105398891'
        :param money: float, withdraw amount. Ie, 345609
        """
        witdraw_amount = TransactionHelper().convert_currency(money)
        AccountController().withdraw(user_id, witdraw_amount)

    @staticmethod
    def deposit_money(user_id, money):
        """
        Deposits in the account
        :param user_id: str, user id. Ie, '105398891'
        :param money: float, withdraw amount. Ie, 2000
        """
        AccountController().deposit(user_id, money)

    @staticmethod
    def get_account_balance(user_id):
        """
        Gets account balance
        :param user_id: str, user id. Ie, '105398891'
        """
        account_balance = AccountController().get_account_balance(user_id)
        return {"account_balance": {"balance": account_balance.get("balance")}}

    @staticmethod
    def validate_condition(condition, result):
        """
        Validates conditions given to execute the next step
        :param condition: List, condition. Ie,
            [
                {"from_id": "account_balance", "field_id": "balance", "operator": "gt", "value": 100000}
            ]
        :param result: Dict, contains params data can be entries for post steps. Ie,
            {
                'start': {'user_id': '105398891', 'pin': 2090},
                'validate_account': {'is_valid': True},
                'account_balance': {'balance': 294700.0},
                ...
            }
        :return: Bool, flag to know if the conditions are valid. Ie, True
        """

        is_valid = True
        for cond in condition:
            print(cond)
            value = result.get(cond['from_id']).get(cond['field_id'])
            print(cond.get("value"))
            print(value)
            print(cond.get("operator"))
            is_valid = is_valid and getattr(ValidatorHelper, cond.get("operator"))(value, cond.get("value"))
        return is_valid

    @staticmethod
    def get_result_field(step_params, dict_params):
        """
        Get params needed to execute a specified step
        :param step_params: Dict,  step params. Ie,
            {
                "user_id": {"from_id": "start", "param_id": "user_id"},
                "pin": {"from_id": "start", "param_id": "pin"}
              }
        :param dict_params: Dict, contains params data can be entries for post steps. Ie,
            {
                'start': {'user_id': '105398891', 'pin': 2090},
                'validate_account': {'is_valid': True},
                'account_balance': {'balance': 294700.0},
                ...
            }
        :return: Dict, step params. Ie,
            {"user_id": '105398891', "pin": 2090 }
        """
        params = None
        for param, config in step_params.items():
            from_id = config.get("from_id")
            param_id = config.get("param_id")
            if not params:
                params = {}
            params[param] = dict_params.get(from_id).get(param_id) if from_id else config.get("value")
        return params
