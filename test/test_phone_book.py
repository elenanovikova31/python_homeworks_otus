import pytest



from python_homeworks_otus import model
from python_homeworks_otus.model import Contact

NAME = "John Doe"
PHONE_NUMBER = "+79272142123"
COMMENT = "Friend"
INCORRECT_ID = 9999999

phone_book = model.Phonebook()
phone_book.open_file()


# Проверка добавления контакт
def test_add_contact_to_phone_book():
    contact_data = [NAME, PHONE_NUMBER, COMMENT]
    contact = Contact(contact=contact_data)
    contact.add_contact(phone_book)

    # Получаем последний id из телефонной книги
    contact_id = (sorted(phone_book.global_phone_book.keys())[-1])
    added_contact = phone_book.global_phone_book.get(contact_id)
    assert added_contact.name == NAME, "Имя не совпадает"
    assert added_contact.phone == PHONE_NUMBER, "Номер телефона не совпадает"
    assert added_contact.comment == COMMENT, "Комментарий не совпадает"

# Проверка изменения контакта
def test_change_contact_to_phone_book():
    contact_id_to_change = 1
    changed_contact_data = [NAME, PHONE_NUMBER, COMMENT]
    changed_contact = Contact(contact=changed_contact_data)
    changed_contact.change_contact(book=phone_book, cnt_id=contact_id_to_change)
    changed_contact = phone_book.global_phone_book.get(contact_id_to_change)
    assert changed_contact.name == NAME, "Имя контакта не было изменено"
    assert changed_contact.phone == PHONE_NUMBER, "Номер телефона не был изменен"
    assert changed_contact.comment == COMMENT, "Комментарий не был изменен"

# Проверка ошибки при отправке несуществующего id контакта при изменении
def test_change_contact_to_phone_book_incorrect_id_error():
    changed_contact_data = [NAME, PHONE_NUMBER, COMMENT]
    changed_contact = Contact(contact=changed_contact_data)
    changed_contact_error = changed_contact.change_contact(book=phone_book, cnt_id=INCORRECT_ID).error
    assert changed_contact_error == f'Контакта с id = {INCORRECT_ID} не существует в справочнике!', \
        "Ожидаемая ошибка не получена!"

# Проверка удаления контакта
def test_delete_contact_to_phone_book():
    phone_book = model.Phonebook()
    phone_book.open_file()
    assert len(phone_book.global_phone_book) == 2, "Количество контактов в телефонной книге != 2"
    contact_id_to_delete = 2
    Contact.delete_contact(book=phone_book.global_phone_book, cnt_id=contact_id_to_delete)
    assert len(phone_book.global_phone_book) == 1, "Контакт с id={contact_id_to_delete} не был удален!"

# Проверка ошибки при отправке несуществующего id контакта при удалении
def test_delete_contact_to_phone_book_incorrect_id_error():
    phone_book = model.Phonebook()
    phone_book.open_file()
    assert len(phone_book.global_phone_book) == 2, "Количество контактов в телефонной книге != 2"
    delete_contact_error = Contact.delete_contact(book=phone_book.global_phone_book, cnt_id=INCORRECT_ID)
    assert delete_contact_error.format(INCORRECT_ID) == f'Контакта с id = {INCORRECT_ID} не существует в справочнике!', \
        "Ожидаемая ошибка не получена!"


@pytest.mark.parametrize(
    "s_word, user_count",
    [
        pytest.param("Вал", 1),
        pytest.param("89", 2),

    ]
)
# Поиск контакта
def test_search_contact(s_word, user_count):
    phone_book = model.Phonebook()
    phone_book.open_file()
    found_contact = Contact.search_contact(book=phone_book, s_word=s_word)
    assert len(found_contact) == user_count, f"Количество контактов в телефонной книге != {user_count}"
