import text
import view
import model


def start_app():
    start_loop = True
    global_phone_book = model.Phonebook()
    while start_loop:
        view.show_menu()
        user_choice = view.menu_choice()
        global_phone_book.open_file()
        match user_choice:
            case 1:
                global_phone_book.save_file()
                view.print_message(text.save_pb_successful)
            case 2:
                view.print_contacts(global_phone_book.global_phone_book)
            case 3:
                contact = model.Contact(contact=view.input_contact(text.new_contact))
                contact.add_contact(global_phone_book=global_phone_book)
                view.print_message(text.add_contact_successful(contact.name))
            case 4:
                search_word = view.input_data(text.input_search_word)
                result = model.Contact.search_contact(book=global_phone_book, s_word= search_word)
                view.print_contacts(result)
            case 5:
                changed_id = view.input_data(text.input_changed_id)
                changed_contact = model.Contact(contact=view.input_contact(text.new_contact))
                changed_contact.change_contact(book=global_phone_book, cnt_id=changed_id)
                view.print_message(text.change_contact_successful(changed_contact))
                global_phone_book.save_file()
            case 6:
                cnt_id = view.input_data(text.input_delete_id)
                name = model.Contact.delete_contact(book=global_phone_book.global_phone_book, cnt_id=cnt_id)
                view.print_message(text.delete_contact_successful(name=name, cnt_id=cnt_id))
                global_phone_book.save_file()
            case 7:
                start_loop = False
                view.print_message(text.good_bye)
