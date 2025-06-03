from re import *
from validator import Validator
from register_form_fields import RegisterFormFields

class PeselValidator(Validator):
    def __init__(self, pesel):
        self.pesel = pesel

    def is_valid(self):

        if self.pesel is None or not self.pesel.strip().isdigit() or len(self.pesel.strip()) != 11:
            return False

        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        pesel_digits = [int(d) for d in self.pesel]

        # Obliczenie sumy ważonej
        weighted_sum = sum(w * d for w, d in zip(weights, pesel_digits[:10]))
        control_digit = (10 - (weighted_sum % 10)) % 10

        return control_digit == pesel_digits[10]


    def field_name(self):
        return RegisterFormFields.PESEL