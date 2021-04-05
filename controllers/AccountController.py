from managers.AccountManager import AccountManager


class AccountController:

    def initialize_balance(self, user_id):
        """
        :param user_id:
        :return:
        """
        account_id = AccountManager().insert_one(user_id)
        return account_id

    def get_account_balance(self, user_id):
        """

        :param user_id:
        :return:
        """
        filters = {"user_id": user_id}
        return AccountManager().get(filters)

    def deposit(self, user_id, money):
        """

        :param user_id:
        :param money:
        :return:
        """
        account = self.get_account_balance(user_id)
        new_balance = account.get("balance") + money
        AccountManager().update({"user_id": user_id}, {"balance": new_balance})

    def withdraw(self, user_id, money):
        """

        :param user_id:
        :param money:
        :return:
        """
        account = self.get_account_balance(user_id)
        new_balance = account.get("balance") - money
        AccountManager().update({"user_id": user_id}, {"balance": new_balance})
