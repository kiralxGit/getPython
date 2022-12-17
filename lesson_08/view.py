def main_menu():
    print('\nМеню: '
          '\n1. Показать телефонную книгу'
          '\n2. Открыть файл телефонной книги'
          '\n3. Сохранить файл телефонной книги'
          '\n4. Добавить контакт'
          '\n5. Изменить контакт'
          '\n6. Удалить контакт'
          '\n7. Найти контакт'
          '\n0. Выход\n')
    return choice_main_menu()

def choice_main_menu():
      while True:
            try:
                  choice = int(input('Выберите пункт: '))
                  print()
                  if choice in range(0, 8):
                        return choice
                  else:
                        print('Такого пункта нет! Повторите попытку')
            except:
                  print('Ошибка ввода! Некорректные данные!')

def print_phone_book(phone_book: list):
      if len(phone_book) > 0:
            for id, contact in enumerate(phone_book, 1):
                  print(id, *contact)
      else:
            print('Телефонная книга пуста или не загружена!')

def load_success():
      print('Телефонная книга загружена!')

def save_success():
      print('Телефонная книга сохранена!')

def change_success():
      print('Контакт изменён!')

def remove_success():
      print('Контакт удалён!')

def remove_confirm(name):
      while True:
            confirm = input(f'Вы действительно хотите удалить {name}? (y/n)')
            if confirm.lower() == 'y':
                  return True
            elif confirm.lower() == 'n':
                  print('Отмена удаления')
                  return False
            else:
                  print('Ошибка ввода! Некорректные данные!')

def input_new_contact():
      name = input('Введите имя контакта: ')
      phone = input('Введите телефон контакта: ')
      comment = input('Введите комментарий к контакту: ')
      return [name, phone, comment]

def input_remove_contact() -> int:
      id = int(input('\nВведите номер контакта для удаления: '))
      return id

def log_off():
      print('До свидания!')