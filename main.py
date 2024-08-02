"""_summary_
    """
from handlers import parse_input, add_contact, change_contact, show_all, show_phone, delete_contact, add_birthday, show_birthday, show_upcoming_birthdays
# from classes import AddressBook
from pickle_serialiser import save_data, load_data

def main():
    """The main function of the bot, manages the main cycle of command processing"""
    # book = AddressBook()
    book = load_data()
    # contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        # завершується при введенні команди "close" або "exit"
        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break
        # вітається при введенні команди "hello"
        if command == "hello":
            print("How can I help you?")
        
        # додає новий контакт при введенні команди "add [ім'я] [номер телефону]"
        elif command == "add":
            print(add_contact(args, book))
        
        # змінює номер телефону контакту при введенні команди "change [ім'я] [старий телефон] [новий телефон]" 
        elif command == "change": 
            print(change_contact(args, book))
        
        # За командою "phone [ім'я]" бот виводить у консоль номер телефону для зазначеного контакту
        elif command == "phone":
            print(show_phone(args, book))
        
        # За командою "all" бот виводить всі збереженні контакти з номерами телефонів у консоль.
        elif command == "all":
            print(show_all(book))
        
        # За командою "delete all" бот видаляє всі контакти.
        # За командою "delete [ім'я]" бот видаляє зазначений контакт.
        elif command == "delete":
            print(delete_contact(args, book))

        # add-birthday [ім'я] [дата народження]: Додати дату народження для вказаного контакту.
        elif command == "add-birthday":
            print(add_birthday(args, book))
        
        # show-birthday [ім'я]: Показати дату народження для вказаного контакту.
        elif command == "show-birthday":
            print(show_birthday(args, book))
        
        # birthdays: Показати дні народження, які відбудуться протягом наступного тижня.
        elif command == "birthdays":
            print(show_upcoming_birthdays(book))

        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()
