from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record


    def del_record(self, record):
        self.data.pop(record.name.value)


class Field:
    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.value = phone


class Record:

    def __init__(self, name: Name, phone: Phone = None):
        self.phones = []
        self.name = name
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone.value:
                self.phones.pop(index)
                self.add_phone(new_phone)
                return f"У контакта \033[34m{self.name.value}\033[0m телефон \033[34m{old_phone.value}\033[0m изменён на \033[34m{new_phone.value}\033[0m"
        return f"Нет номера \033[34m{old_phone.value}\033[0m у контакта \033[34m{self.name.value}\033[0m"

    def del_phone(self):    
        self.phones.clear()
    

