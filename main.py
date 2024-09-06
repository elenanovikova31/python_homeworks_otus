import re

global_phone_book = {}

menu_item = [
    "Открыть файл",
    "Сохранить файл",
    "Показать все контакты",
    "Добавить контакт",
    "Найти контакт",
    "Редактировать контакт",
    "Удалить контакт",
    "Выход",
]

decision_item = ["Да", "Нет"]


def input_user_choice():
    while True:
        choice = input("Выберите пункт меню: ")
        if choice.isdigit() and 0 < int(choice) < 9:
            return choice
        print("Введите пункт от 1 до 8")


def input_user_agreement():
    while True:
        choice = input("Вы действительно хотите сохранить изменения (Да/Нет)?")
        return choice


def next_id(phone_book):
    if phone_book:
        return max(phone_book) + 1
    return 1


def open_file():
    """
    Функция открытия справочника
    """
    with open("phone_book.txt", "r", encoding="UTF-8") as file:
        data = sorted(file.readlines(), key=lambda x: x[0])
        data = list(map(lambda x: x.strip().split(";"), data))
        for contact in data:
            global_phone_book[next_id(global_phone_book)] = {
                "name": contact[0],
                "phone": contact[1],
                "comment": contact[2],
            }
        return global_phone_book


def save_file():
    """
    Функция сохранения справочника
    """
    user_decision = input_user_agreement()
    if user_decision == "Да":
        data = []
        for contact in global_phone_book.values():
            data.append(";".join(contact.values()))
        data = "\n".join(data)
        with open("phone_book.txt", "w", encoding="UTF-8") as file:
            file.write(data)
        print("Контакт успешно сохранен")
    else:
        print("Контакт не был сохранен")
        start()


def add_contact():
    """
    Функция добавления нового контакта в справочник
    """
    contact = {}
    fields = {
        "name": "Введите имя: ",
        "phone": "Введите телефон: ",
        "comment": "Введите комментарий: ",
    }
    for key, field in fields.items():
        if key == "phone":
            result = True
            while result:
                phone = input(field)
                result = bool(
                    re.match(
                        r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$",
                        phone,
                    )
                )
                if result:
                    contact[key] = phone
                    break
                else:
                    print("Введен телефонный номер некорректного формата")
        elif key == "name":

            contact[key] = input(field)
        elif key == "comment":
            contact[key] = input(field)
    global_phone_book[next_id(global_phone_book)] = contact


def update_contact(contact_id: int):
    """
    Функция обновления данных существующего контакта в справочнике
    """

    fields = {
        "name": "Введите имя: ",
        "phone": "Введите телефон: ",
        "comment": "Введите комментарий: ",
    }
    for key, field in fields.items():
        if key == "phone":
            result = True
            while result:
                phone = input(field)
                result = bool(
                    re.match(
                        r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$",
                        phone,
                    )
                )
                if result:
                    global_phone_book.get(contact_id)[key] = phone
                    break
                else:
                    print("Введен телефонный номер некорректного формата")
        elif key == "name":

            global_phone_book.get(contact_id)[key] = input(field)
        elif key == "comment":
            global_phone_book.get(contact_id)[key] = input(field)


def delete_contract(contact_id: int):
    """
    Функция удаления контакта из справочника
    """
    global_phone_book.pop(contact_id, None)


def show_contacts(phone_book):
    """
    Функция вывода всех контактов из справочника
    """
    if phone_book:
        print("=" * 100)
        for u_id, contact in phone_book.items():
            print(
                f'{u_id: >2}. {contact["name"]: <20} {contact["phone"]: <20} {contact["comment"]: <20}'
            )
        print("=" * 100)
    else:
        print("Телефонная книга пуста или не открыта")


def choose_contact():
    """
    Функция выбора id контакта, требуется для редактирования контакта
    """
    contact_id = input("Выберите id контакта: ")
    return contact_id


def find_contact():
    """
    Функция поиска контакта в справочнике по искомому фрагменту
    """
    result = {}
    key_word = input("Введите слово для поиска: ")
    for u_id, contact in global_phone_book.items():
        for key, field in contact.items():
            if key == "phone":
                res = []
                for i in field:
                    if i.isdigit():
                        res.append(i)
                field = "".join(res)
            if key_word.lower() in field.lower():
                result[u_id] = contact
                break
    show_contacts(result)


def start():
    while True:
        print("Главное меню:")
        for i, item in enumerate(menu_item, 1):
            print(f"\t{i}. {item}")
        user_choice = input_user_choice()
        if user_choice == "1":
            if open_file():
                print("Телефонная книга успешно открыта")
            else:
                print("Телефонная книга пуста")
        elif user_choice == "2":
            save_file()
        elif user_choice == "3":
            show_contacts(global_phone_book)
        elif user_choice == "4":
            add_contact()
            save_file()
        elif user_choice == "5":
            find_contact()
        elif user_choice == "6":
            find_contact()
            contact_id = choose_contact()
            update_contact(contact_id=int(contact_id))
            save_file()
        elif user_choice == "7":
            find_contact()
            contact_id = choose_contact()
            delete_contract(contact_id=int(contact_id))
            save_file()
        elif user_choice == "8":
            print("До свидания")
            break


start()
