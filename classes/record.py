"""Record class"""

from classes.name import Name
from classes.phone import Phone
from classes.birthday import Birthday

class Record:
    """Record class"""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        contact_string = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

        if self.birthday:
            contact_string += f", birthday: {self.birthday}"

        return contact_string

    def add_phone(self, number: str):
        """Add a phone number to the record."""
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        """Remove a phone number from the record."""

        self.phones = list(filter(lambda phone: phone == number, self.phones))

    def edit_phone(self, old_number: str, new_number: str):
        """Edit a phone number in the record."""

        self.phones = list(
            map(
                lambda phone: Phone(new_number) if phone.value == old_number else phone,
                self.phones,
            )
        )

    def find_phone(self, number):
        """Find a phone number in the record."""

        for phone in self.phones:
            if phone.value == number:
                return phone

    def add_birthday(self, date_of_birthday):
        """Add a birthday to the record."""
        self.birthday = Birthday(date_of_birthday)
