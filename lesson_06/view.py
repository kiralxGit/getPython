def input_first_value():
    number = input('Введите число или строку без пробелов: ')
    return number

def input_number() -> int:
    while True:
        try:
            number = int(input('Введите целое число: '))
            return number
        except:
            print('Ошибка')

def input_operation():
    while True:
        operation = input('Введите операнд: ')
        if operation in ['*', '/', '+', '-', '=']:
            return operation
        else:
            print('Введите корректный операнд')

def print_to_console(value_text):
    print(value_text)

def log_off(value):
    print(f'Результат: {value}. До свидания!')

def print_division_zero():
    print('На 0 делить нельзя!')

def input_error():
    print('Проверьте правильность ввода!')