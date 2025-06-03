from re import *
from validator import Validator
from register_form_fields import RegisterFormFields

class LoginValidator(Validator):
    def __init__(self, login):
        self.login = login
        self.LOGIN_MIN_LENGTH = 4

    def is_valid(self):

        if self.login is None or len(self.login) < self.LOGIN_MIN_LENGTH:
            return False



        return True

    def field_name(self):
        return RegisterFormFields.LOGIN