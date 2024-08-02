"""Phone class"""
from classes.field import Field

class Phone(Field):
    """Phone class"""

    def __init__(self, number):
        self.value = self.validate_number(number)

    def validate_number(self, number):
        """validates a phone number

        Args:
            number (int): phone number for validation

        Raises:
            ValueError: The phone number must contain 10 digits
            ValueError: The phone number must contain only numbers

        Returns:
            int: validated number
        """

        if len(number) != 10:
            raise ValueError("The phone number must contain 10 digits")

        if not number.isdigit():
            raise ValueError("The phone number must contain only numbers")

        return number
