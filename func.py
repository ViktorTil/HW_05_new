from classes import AddressBook, Name, Phone, Record

phone_book = AddressBook()

def error_with_func(arg1,arg2):
    def input_error(func):
        def proc_error(*args):
            try:
               return func(*args)
            except IndexError:
                return f'Добавьте все данные в команду \033[34m{arg1}\033[0m по шаблону: \033[34m<{arg2}>\033[0m'
            except ValueError:
                pass
        return proc_error
    return input_error


@error_with_func('add', "add [name] [phone]")  
def add_phone(cont):
    
    contact = cont.split(' ')[1:]  
    
    name = contact[0].capitalize()
    if len(contact) >= 2:
        if not name in phone_book.keys():
            phone = Phone(contact[1])
            rec = Record(Name(name), phone)
            phone_book.add_record(rec)
            message_add = f"Новый контакт \033[34m{name}\033[0m с номером \033[34m{contact[1]}\033[0m создан"
            
        else: 
            rec = phone_book.get(name)
            rec.add_phone(Phone(contact[1]))
            message_add = f"Номер \033[34m{contact[1]}\033[0m добавлен к контакту \033[34m{name}\033[0m"
    else:
        message_add =  "Добавьте в команду \033[34madd\033[0m номер телефона"
        if not name in phone_book.keys():
            rec = Record(Name(name))
            phone_book.add_record(rec)
            message_add = f"Контакт \033[34m{name}\033[0m без номера добавлен"
        
    return message_add
        



@error_with_func('change', 'change [name] [old_phone] [new_phone]')
def change(contact):
    chng_cont = contact.split(' ')[1:]
    name = chng_cont[0].capitalize()
    old_phone = chng_cont[1]
    new_phone = chng_cont[2]
    
    if name in phone_book.keys():
        rec = phone_book.get(name)
        message_chng = rec.change_phone(Phone(old_phone), Phone(new_phone))
    
    else :
        message_chng = f'Нет контакта \033[34m{name}\033[0m в Вашем списке'
    return message_chng


@error_with_func('del', 'del [name]')
def delete(contact):
    c_number=contact.split(" ")[1].capitalize()
    message_del_cont = f"Не могу удалить номер несуществующего контакта \033[34m{c_number}\033[0m"
    if c_number in phone_book.keys():
        phone_book.del_record(phone_book.get(c_number))
        message_del_cont = f"Контакт \033[34m{c_number}\033[0m удалён из Вашей книги"
    return message_del_cont
 
        
@error_with_func('del phones', 'del phones [name]')
def delete_phones(contact):
    del_ph = contact.title().split(' ')[2:]
    message_del_phones = f"Не могу удалить телефоны несуществующего контакта \033[34m{del_ph[0]}\033[0m"
    if del_ph[0] in phone_book.keys():
        phone_book.get(del_ph[0]).del_phone()
        message_del_phones = f"Номера контакта \033[34m{del_ph[0]}\033[0m удалены из книги"
    return message_del_phones


@error_with_func('phone', 'phone [name]')
def phone(contact):
    c_number=contact.split(" ")[1].capitalize()
    message_cont = f'В ваших контактах отсутствует \033[34m{c_number}\033[0m'
    if c_number in phone_book.keys():
        message_cont = f"Номер(а) контакта \033[34m{c_number} : {', '.join(list(phone.value for phone in phone_book.get(c_number).phones))}\033[0m"
    return message_cont

def show_all(x):
    result = []
    for rec in phone_book.values():
        result.append(f'Name: \033[34m{rec.name.value}\033[0m, phone number \033[34m{", ".join([p.value for p in rec.phones])}\033[0m')
    return "\n".join(result)

