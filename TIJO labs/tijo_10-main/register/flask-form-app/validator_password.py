from re import *
from validator import Validator
from register_form_fields import RegisterFormFields

class PasswordValidator(Validator):
    def __init__(self, password):
        self.password = password
        self.PASSWORD_MIN_LENGTH = 4

    def is_valid(self):

        if self.password is None or len(self.password) < self.PASSWORD_MIN_LENGTH:
            return False

        regex = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-]).{4,}$"
        pattern = compile(regex)
        matcher = pattern.match(self.password)

        return bool(matcher)

    def field_name(self):
        return RegisterFormFields.PASSWORD