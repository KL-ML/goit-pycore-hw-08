from datetime import datetime
from classes.field import Field

class Birthday(Field):
    def __init__(self, value: str):
        try:
            self.value = datetime.strptime(value, "%Y.%m.%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY.MM.DD")
        
    def __str__(self):
        return f"{self.value.strftime("%Y.%m.%d")}"