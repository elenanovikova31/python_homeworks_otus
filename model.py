from collections import namedtuple

global_phone_book = {}
path = 'phone_book.txt'
separator = ';'
contact = namedtuple('Contact', 'name, phone, comment')


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = list(map(lambda x: x.strip().split(separator), file.readlines()))
        for cnt in data:
            global_phone_book[int(cnt[0])] = contact(*cnt[1:])


def save_file():
    data = []
    for cnt_id, cnt in global_phone_book.items():
        data.append(separator.join([str(cnt_id), *cnt]))
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(data))


def next_id():
    return max(global_phone_book) + 1


def add_contact(new_contact: list):
    cnt = contact(*new_contact)
    global_phone_book[next_id()] = cnt


def search_contact(s_word: str):
    result = {}
    for i, cnt in global_phone_book.items():
        if s_word.lower() in ' '.join(cnt).lower():
            result[i] = cnt
    return result


def change_contact(cnt_id: str, cnt: list):
    new_contact = []
    current_contact = global_phone_book[int(cnt_id)]
    for i in range(len(cnt)):
        new_contact.append(cnt[i] if cnt[i] else current_contact[i])
    global_phone_book[int(cnt_id)] = contact(*new_contact)
    return new_contact[0]


def delete_contact(cnt_id: str):
    cnt = global_phone_book.pop(int(cnt_id))
    return cnt.name
