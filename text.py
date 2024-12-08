from error_message import ErrorMessage

message_div = '='

main_menu = [
    'Главное меню:',
    'Сохранить справочник',
    'Показать все контакты',
    'Создать контакт',
    'Найти контакт',
    'Изменить контакт',
    'Удалить контакт',
    'Выход',
]

menu_item_choice = 'Выберите пункт меню: '
menu_item_error = f'Введите число от 1 до {len(main_menu) - 1}!'

open_pb_successful = 'Телефонная книга успешно открыта!'
save_pb_successful = 'Телефонная книга успешно сохранена!'

new_contact = [
    'Введите имя: ',
    'Введите номер телефона: ',
    'Введите комментарий: ',
]

input_changed_id = 'Введите ID контакта, который хотите изменить: '
input_delete_id = 'Введите ID контакта, который хотите удалить: '

no_changes = '(или Enter - оставить без изменений): '

change_contact = [
    'Введите новое имя ' + no_changes,
    'Введите новый телефон ' + no_changes,
    'Введите новый комментарий ' + no_changes,
]


def add_contact_successful(name: str):
    return f'Контакт {name} успешно добавлен!'


def change_contact_successful(changed_contact):
    if changed_contact.error is None:
        return f'Контакт {changed_contact.name} успешно изменен!'
    else:
        return changed_contact.error


def delete_contact_successful(name: str, cnt_id: int):
    if name != ErrorMessage.CONTACT_NOT_EXISTS:
        return f'Контакт {name} успешно удален!'
    else:
        return name.format(cnt_id)

input_search_word = 'Введите слово для поиска: '

good_bye = 'До свидания!'
