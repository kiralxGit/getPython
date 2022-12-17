import view

phone_book = []

def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book

def add_contact(contact: list):
    global phone_book
    phone_book.append(contact)

def remove_contact(id):
    global phone_book
    name = phone_book[id - 1][0]
    if view.remove_confirm(name):
        phone_book.pop(id - 1)
        return True
    return False