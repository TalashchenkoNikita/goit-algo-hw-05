def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me a name"
        except KeyError:
            return "Name not found"
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def find_contact(args, contacts):
    name = args[0]
    return f"Phone number for {name}: {contacts[name]}"


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"{name} already exists in contacts. You can update the contact using the 'update' command."
    else:
        contacts[name] = phone
        return "Contact added."


@input_error
def update_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} updated to {new_phone}."
    else:
        return f"{name} not found in contacts. You can add the contact using the 'add' command."


@input_error
def get_all(contacts):
    for name, phone in contacts.items():
        print(name, phone)
    return "These are all contacts."


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
            print(add_contact(args, contacts))
        elif command == "find":
            print(find_contact(args, contacts))
        elif command == "update":
            print(update_contact(args, contacts))
        elif command == "all":
            print(get_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()