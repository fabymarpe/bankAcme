from controllers.AccountController import AccountController
from managers.UserManager import UserManager


class UserController:

    def create_new_user(self, user_id, pin):
        user_manager = UserManager()
        filters = {"user_id": user_id}
        if user_manager.not_exist(filters):
            user_manager.insert_one(user_id, pin)
            AccountController().initialize_balance(user_id)
