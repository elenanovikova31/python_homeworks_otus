message_div = '='

main_menu = [
    'Главное меню:',
    'Открыть справочник',
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


def change_contact_successful(name: str):
    return f'Контакт {name} успешно изменен!'


def delete_contact_successful(name: str):
    return f'Контакт {name} успешно удален!'


input_search_word = 'Введите слово для поиска: '

good_bye = 'До свидания!'
