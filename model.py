from collections import namedtuple
from error_message import ErrorMessage


class Phonebook:

    def __init__(self):
        self.global_phone_book = {}
        self.path = 'phone_book.txt'
        self.separator = ';'
        self.contact = namedtuple('Contact', 'name, phone, comment')

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = list(map(lambda x: x.strip().split(self.separator), file.readlines()))
            for cnt in data:
                self.global_phone_book[int(cnt[0])] = self.contact(*cnt[1:])

    def save_file(self):
        data = []
        for cnt_id, cnt in self.global_phone_book.items():
            data.append(self.separator.join([str(cnt_id), *[cnt.name, cnt.phone, cnt.comment]]))
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(data))

    def next_id(self):
        return max(self.global_phone_book) + 1


class Contact:

    def __init__(self, contact):

        self.name = contact[0]
        self.phone = contact[1]
        self.comment = contact[2]
        self.error = None

    def add_contact(self, global_phone_book):
        global_phone_book.global_phone_book[global_phone_book.next_id()] = self

    def change_contact(self, book, cnt_id: str):
        try:
            book.global_phone_book[int(cnt_id)]
        except KeyError:
            self.error = ErrorMessage.CONTACT_NOT_EXISTS.format(cnt_id)
        if self.error is not None:
            return self
        else:
            book.global_phone_book[int(cnt_id)] = self

    @staticmethod
    def search_contact(book, s_word: str):
        result = {}
        for i, cnt in book.global_phone_book.items():
            if s_word.lower() in ' '.join(cnt).lower():
                result[i] = cnt
        return result

    @staticmethod
    def delete_contact(book, cnt_id: str):
        try:
            cnt = book.pop(int(cnt_id))
            return cnt.name
        except BaseException:
            return ErrorMessage.CONTACT_NOT_EXISTS
