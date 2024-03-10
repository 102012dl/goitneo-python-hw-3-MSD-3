\Домашнє завдання №3 


class Birthday:
    def __init__(self, date):
        self.date = date


class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.birthday = None

    def add_birthday(self, date):
        self.birthday = Birthday(date)


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append(Record(name, phone))

    def change_phone(self, name, new_phone):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = new_phone
                return f"Phone number updated for {name}."

        return f"Contact with name {name} not found."

    def get_birthday(self, name):
        for contact in self.contacts:
            if contact.name == name and contact.birthday:
                return f"{contact.name}'s birthday is on {contact.birthday.date}"

        return f"Birthday not found for {name}."

    def get_birthdays_per_week(self):
        # Logic to get birthdays per week
        pass


# Handler functions for commands
def add_birthday_command(contact_name, date):
    for contact in address_book.contacts:
        if contact.name == contact_name:
            contact.add_birthday(date)
            return "Birthday added successfully."

    return f"Contact with name {contact_name} not found."


def show_birthday_command(contact_name):
    return address_book.get_birthday(contact_name)


def birthdays_command():
    # Logic to display upcoming birthdays
    pass


# Main program loop
address_book = AddressBook()

while True:
    command = input("Enter a command: ").split()

    if command[0] == 'add-birthday':
        result = add_birthday_command(command[1], command[2])
        print(result)
    elif command[0] == 'show-birthday':
        result = show_birthday_command(command[1])
        print(result)
    elif command[0] == 'birthdays':
        birthdays_command()
    # Add other commands handlers here
    elif command[0] == 'close' or command[0] == 'exit':
        print("Program closed.")
        break
    else:
        print("Invalid command. Try again.")





\Додаткове завдання (не обов'язкове) 



\Завдання 


import pickle


class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def save_to_disk(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_from_disk(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            print("File not found. Starting with an empty address book.")


# Create an instance of the AddressBook class
address_book = AddressBook()

# Add some contacts
address_book.add_contact("John Doe", "123-456-7890")
address_book.add_contact("Jane Smith", "987-654-3210")

# Save address book to disk
address_book.save_to_disk("address_book.pickle")

# Load address book from disk
new_address_book = AddressBook()
new_address_book.load_from_disk("address_book.pickle")

# Print the loaded contacts
print("Loaded contacts:")
for name, phone in new_address_book.contacts.items():
    print(f"{name}: {phone}")
