import re

import text

def input_data(msg: str):
    return input(msg)


def menu_choice():
    while True:
        menu_item = input_data(text.menu_item_choice)
        if menu_item.isdigit() and 0 < int(menu_item) < len(text.main_menu):
            return int(menu_item)
        print(text.menu_item_error)


def show_menu():
    for i, item in enumerate(text.main_menu):
        if not i:
            print(item)
        else:
            print(f'\t{i}. {item}')


def print_contacts(book, column_size: int = 20):
    try:
        assert book != {}
        print('\n' + text.message_div * (3 + column_size * 3))
        for i, contact in book.items():
            print(f'{i: >3} {contact.name: <{column_size}} '
              f'{contact.phone: <{column_size}} {contact.comment: <{column_size}}')
        print(text.message_div * (3 + column_size * 3), end='\n\n')
    except AssertionError:
        print(text.message_div * (3 + column_size * 3), end='\n\n')
        print("Контакт не найден!!!")
        print(text.message_div * (3 + column_size * 3), end='\n\n')


def print_message(msg: str):
    print('\n' + text.message_div * len(msg))
    print(msg)
    print(text.message_div * len(msg), end='\n\n')


def input_contact(msg):
    data = []
    for item in msg:
        if item in ["Введите номер телефона: ", "Введите новый телефон (или Enter - оставить без изменений): "]:
            result = True
            while result:
                phone = input_data(item)
                result = bool(
                    re.match(
                        r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$",
                        phone,
                    )
                )
                if result:
                    data.append(phone)
                    break
                else:
                    print("Введен телефонный номер некорректного формата")
        else:
            data.append(input_data(item))
    return data
