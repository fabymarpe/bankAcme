from werkzeug.exceptions import HTTPException


class InvalidAccount(HTTPException):
    def __init__(self, user_id, pin):
        HTTPException.__init__(self)
        self.code = 409
        self.data = {"message": "Account for user {} and pin {} is not valid.".format(user_id, pin)}


class InsufficientBalance(HTTPException):
    def __init__(self, user_id, amount):
        HTTPException.__init__(self)
        self.code = 409
        self.data = {
            "message": "Withdrawal by {} can not be processed because account balance for user {} is "
                       "insufficient".format(amount, user_id)
        }
