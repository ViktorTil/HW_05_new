from classes import AddressBook, Name, Phone, Record
from func import add_phone, change, delete, delete_phones, phone, show_all

commands = ["hello", ["good bye", "close", "exit", "bye", "esc", "q"], "add", "change", "del", "del phones", "phone", "show all"]
answers = ["How can I help you?", "Good bye!", add_phone, change, delete, delete_phones, phone, show_all]



def reply(command):
    bot=True
    operator=command.lower().split(" ")
    if command.lower() in commands[1]:
        print(answers[1])
        bot = False
    elif operator[0] in commands or (" ".join(command.lower().split(" ")[:2])) in commands: #command.lower() in commands:
        try:
            index_comm = commands.index(" ".join(command.lower().split(" ")[:2])) #command.lower()
        except ValueError:
            index_comm = commands.index(operator[0])

        try:
            print(answers[index_comm](command))
        except:
            print(answers[index_comm])
    else:
        print(f'Введите правильную команду :\033[34m{commands[0]}, {", ".join(commands[2:])}\033[0m или \033[34m{", ".join(commands[1])}\033[0m для выхода')

    return bot



def main():
    working_bot= True
    while working_bot:
        command = input("->")
        working_bot = reply(command)


if __name__ == '__main__':
    main()