from collections import namedtuple

# global_phone_book = {}
# path = 'phone_book.txt'
# separator = ';'
# contact = namedtuple('Contact', 'name, phone, comment')


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

# def next_id():
#     return max(global_phone_book) + 1

# def open_file():
#     with open(path, 'r', encoding='UTF-8') as file:
#         data = list(map(lambda x: x.strip().split(separator), file.readlines()))
#         for cnt in data:
#             global_phone_book[int(cnt[0])] = contact(*cnt[1:])


# def save_file():
#     data = []
#     for cnt_id, cnt in global_phone_book.items():
#         data.append(separator.join([str(cnt_id), *cnt]))
#     with open(path, 'w', encoding='UTF-8') as file:
#         file.write('\n'.join(data))


class Contact:

    def __init__(self, contact):

        self.name = contact[0]
        self.phone = contact[1]
        self.comment = contact[2]

    def add_contact(self, global_phone_book):
        global_phone_book.global_phone_book[global_phone_book.next_id()] = self

    # def change_contact(self, cnt_id: str):
    #     new_contact = []
    #     cnt = [self.name, self.phone, self.comment]
    #     current_contact = global_phone_book[int(cnt_id)]
    #     for i in range(len(cnt)):
    #         new_contact.append(cnt[i] if cnt[i] else current_contact[i])
    #     global_phone_book[int(cnt_id)] = contact(*new_contact)
    #     return new_contact[0]
    #
    # @staticmethod
    # def search_contact(s_word: str):
    #     result = {}
    #     for i, cnt in global_phone_book.items():
    #         if s_word.lower() in ' '.join(cnt).lower():
    #             result[i] = cnt
    #     return result
    #
    # @staticmethod
    # def delete_contact(cnt_id: str):
    #     cnt = global_phone_book.pop(int(cnt_id))
    #     return cnt.name
