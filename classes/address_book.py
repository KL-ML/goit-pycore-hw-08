"""class AddressBook"""

from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    """Stores the contact book and methods for working with it"""
    def __str__(self):
        lines = [str(record) for record in self.data.values()]
        return "\n".join(lines)

    def add_record(self, record):
        """Adds a new record to contact book"""
        if record.name.value in self.data:
            raise KeyError(f"Record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record

    def find(self, name):
        """Finds a record by name"""
        record = self.data.get(name, None)
        return record

    def delete(self, name):
        """Deletes a record by name"""
        if name not in self.data:
            raise KeyError(f"Record with name '{name}' not found.")
        del self.data[name]

    def get_upcoming_birthdays(self):
        """Сreates a list of contacts to wish happy birthday the next 7 days

        Returns:
            list: list of dicts of contacts
        """
        today_datetime = datetime.today().date()
        upcoming_birthdays = []

        for name, record in self.data.items():
            if record.birthday:
                user_birthday = datetime.strptime(str(record.birthday), "%Y.%m.%d").date()
                birthday_prepared = user_birthday.replace(year=today_datetime.year)
                if birthday_prepared < today_datetime:
                    birthday_prepared = birthday_prepared.replace(year=today_datetime.year + 1)

                if (birthday_prepared - today_datetime).days > 7:
                    continue

                if birthday_prepared.weekday() > 5:
                    birthday_prepared += timedelta(days=7 - birthday_prepared.weekday())

                congratulation_date_str = birthday_prepared.strftime("%Y.%m.%d")
                upcoming_birthdays.append(
                    {"name": name, "congratulation_date": congratulation_date_str})

        return upcoming_birthdays
