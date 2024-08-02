"""A module for working with a list of contacts: adding, editing, outputting, deleting."""
# pylint: disable=line-too-long
from classes import AddressBook
from classes import Record
from .decorators import input_error, empty_contact_list

@input_error
def add_contact(args, book: AddressBook):
    """Adds a new contact to the contact list.

    Args:
        args (list): contains name and phone number
        book (class): contact list

    Returns:
        str: message that the contact has been added or updated
    """
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@empty_contact_list
@input_error
def change_contact(args, book: AddressBook):
    """Changes a contact's phone number by the name

#     Args:
#         args (list): contains name, old phone number and new phone number
#         book (class): contact list

#     Returns:
#         str: notification that the contact has been changed, or contact not found
#     """
    name, old_number, new_number, *_ = args
    record = book.find(name)

    record.edit_phone(old_number, new_number)
    return "Phone changed"

@empty_contact_list
@input_error
def show_phone(args, book: AddressBook):
    """Shows a contact information

    Args:
        args (list): contains name and phone number
        book (class): contact list

    Returns:
        str: a message with information about the contact, or that the contact was not found
    """
    name, *_ = args

    record = book.find(name)
    if record is None:
        return f"The {name} is not found"
    return record

@empty_contact_list
def show_all(book: AddressBook):
    """Shows all contacts in the list

    Args:
        contacts (dict): contact list

    Returns:
        str: message with a list of contacts
    """
    return f"{book}"

@empty_contact_list
@input_error
def delete_contact(args, book: AddressBook):
    """Function to delete one contact or all at once

    Args:
        args (list): contains name and phone number
        contacts (dict): contact list

    Returns:
        str: message about deleting one or all contacts
    """
    name, *_ = args

    record = book.find(name)
    if record:
        book.delete(name)
        return f"The {name} has been deleted"

    if name == "all": # видалити всі контакти
        book.data.clear()
        return "All contacts have been deleted"

    return f"The {name} is not found"
