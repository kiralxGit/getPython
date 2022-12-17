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

def change_contact(id_what_change):
    global phone_book
    data = phone_book[id_what_change[0] - 1][id_what_change[1] - 1]
    if data := view.change_contact(data):
        phone_book[id_what_change[0] - 1][id_what_change[1] - 1] = data
        return True
    return False
def remove_contact(id):
    global phone_book
    name = phone_book[id - 1][0]
    if view.remove_confirm(name):
        phone_book.pop(id - 1)
        return True
    return False

def find_contacts(search_substring: str) -> list:
    global phone_book
    search_list = []
    for id, contact in enumerate(phone_book, 1):
        temp = ';'.join(contact).lower()
        if temp.find(str(search_substring).lower()) != (-1):
            temp = contact[:]
            temp.insert(0, id)
            search_list.append(temp)
    return search_list
