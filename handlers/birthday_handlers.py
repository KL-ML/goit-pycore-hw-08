"""A module for working with a contacts birthdays."""
# pylint: disable=line-too-long

from classes import AddressBook
from .decorators import input_error

@input_error
def add_birthday(args, book: AddressBook):
    """Adds a birthday to the contact.

    Args:
        args (list): contains name and birthday
        book (class): contact list

    Returns:
        str: message that the birthday has been added to contact
    """
    name, date, *_ = args
    record = book.find(name)
    if record:
        record.add_birthday(date)
        return "Birthday added"
    else:
        return f"There is no contact {name}"
    
@input_error
def show_birthday(args, book: AddressBook):
    """Shows a birthday of the contact.

    Args:
        args (list): contains name
        book (class): contact list

    Returns:
        str: message that shows contact name and birthday
    """
    name, *_ = args
    record = book.find(name)
    if record:
        if not record.birthday:
            return f"There is no birthday for contact {name}"
        return f"{name} birthday: {record.birthday}"
        
    else:
        return f"There is no contact {name}"
    
def show_upcoming_birthdays(book: AddressBook):
    """Shows all contacts with congratulations dates to the next 7 days

    Args:
        contacts (dict): contact list

    Returns:
        str: message with a list of contacts with congratulations dates
    """
    upcoming_birthdays = book.get_upcoming_birthdays()
    if len(upcoming_birthdays) == 0:
        return "The birthday list is empty."

    lines = [f"Contact name: {birthday["name"]}, congratulation_date: {birthday["congratulation_date"]}" for birthday in upcoming_birthdays]
    return "\n".join(lines)
