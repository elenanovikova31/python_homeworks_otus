import text
import view
import model
from text import change_contact


def start_app():
    start_loop = True
    while start_loop:
        view.show_menu()
        user_choice = view.menu_choice()
        match user_choice:
            case 1:
                model.open_file()
                view.print_message(text.open_pb_successful)
            case 2:
                model.save_file()
                view.print_message(text.save_pb_successful)
            case 3:
                view.print_contacts(model.global_phone_book)
            case 4:
                contact = model.Contact(contact=view.input_contact(text.new_contact))
                contact.add_contact()
                view.print_message(text.add_contact_successful(contact.name))
            case 5:
                search_word = view.input_data(text.input_search_word)
                result = model.Contact.search_contact(search_word)
                view.print_contacts(result)
            case 6:
                changed_id = view.input_data(text.input_changed_id)
                changed_contact = model.Contact(contact=view.input_contact(text.new_contact))
                changed_contact.change_contact(cnt_id=changed_id)
                view.print_message(text.change_contact_successful(changed_contact.name))
            case 7:
                cnt_id = view.input_data(text.input_delete_id)
                name = model.Contact.delete_contact(cnt_id)
                view.print_message(text.delete_contact_successful(name))
            case 8:
                start_loop = False
                view.print_message(text.good_bye)
