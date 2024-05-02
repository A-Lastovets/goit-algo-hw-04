def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"User '{name}'  is already in the contacts: {contacts}"
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return f"User '{name}' is not found in contacts: {contacts}"
    contacts[name] = phone
    return "Contact updated."


def show_phone(name, contacts):
    if name in contacts:
        print(contacts[name])
    else:
        print(f"User '{name}' is not found in contacts: {contacts}")


def show_all(contacts):
    for info in contacts:
        print(f"User '{info}', phone number '{contacts[info]}'")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(args)
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            if len(args) == 1:
                show_phone(args[0], contacts)
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command, please try again. \n\n\
If you want to add a new user : the command must begin with the word 'add' and add user name with phone number\n\
If you want to change the phone number for a user, enter the 'change' command and add user name with phone number\n\
If you want to show the phone number for a user, enter 'show' command and add the user name\n\
If you want to see the list of users, enter 'all' command\n\
If you want to exit the bot : type 'exit' or 'close'\n ")

if __name__ == "__main__":
    main()
