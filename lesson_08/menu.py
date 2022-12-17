import view
import phone_book as pb
import data_base as db



def main_menu(choice: int):
    match choice:
        case 1: # Показать телефонную книгу
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
        case 2: # Открыть файл телефонной книги
            db.load_db()
            view.load_success()
        case 3: # Сохранить файл телефонной книги
            db.save_db()
            view.save_success()
        case 4: # Добавить контакт
            contact = view.input_new_contact()
            pb.add_contact(contact)
        case 5: # Изменить контакт
            pass
        case 6: # Удалить контакт
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
            id = view.input_remove_contact()
            if pb.remove_contact(id):
                view.remove_success()

        case 7: # Найти контакт
            pass
        case 0: # Выход
            return True

def start():
    while True:
        choice = view.main_menu()
        if main_menu(choice):
            view.log_off()
            break