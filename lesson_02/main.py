from decimal import Decimal
from random import randint as rnd

def numbers_sum():
    print()
    print('1. Программа, принимает на вход вещественное число и показывает сумму его цифр\n',
        'Пример:\n',
        '6782 -> 23\n',
        '0.56 -> 11\n')

    num = input('Введите число: ')
    num = num.replace(',', '.')  # на всякий запятую превращаем в точку

    num_str = num.replace('.', '')
    sum = 0
    for i in num_str:
        sum += int(i)
    print(sum, '- через строку')

    num_dec = Decimal(num)
    sum = 0
    pow = 1
    while (num_dec * pow != int(num_dec * pow)):  # честно подглядено на лекции)
        pow *= 10
    num = int(num_dec * pow)
    while num > 0:
        sum += num % 10
        num //= 10
    print(sum, '- через число')
    input('Нажмите Enter для выхода в меню')
    print()


def sequence_list():
    print()
    print('2. Формируем список из n чисел последовательности (1 + 1/n)^n.\n',
        'В консоль выводим сам список и сумму его элементов\n')
    num = int(input('Задайте число n для формирования списка: '))
    nums_list = [(1 + 1 / i) ** i for i in range(1, num + 1)]
    print(*nums_list, sep=', ')
    sum = 0
    for i in nums_list:
        sum += i
    print(f'Сумма всех элементов: {sum:.2f}')
    input('Нажмите Enter для выхода в меню')
    print()

def shuffle_list():
    print()
    print('3. Реализуем алгоритм перемешивания списка без использования встроенного SHUFFLE')
    num = int(input('Введите размер списка: '))
    rnd_list = [rnd(10, 99) for i in range(num)]
    print(f'Первичный массив: {rnd_list}')
    for i in range(len(rnd_list)):
        num_rnd = rnd(i, num - 1)
        temp = rnd_list[i]
        rnd_list[i] = rnd_list[num_rnd]
        rnd_list[num_rnd] = temp
    print(f'Перемешанный массив: {rnd_list}')
    input('Нажмите Enter для выхода в меню')
    print()

def four_stages():
    print()
    print('4. Программа из 4 этапов')
    print('Этап 1-ый, создаём список из рандомных четырех значных чисел')
    lenght = int(input('Введите размер списка: '))
    rnd_list = [rnd(1000, 9999) for i in range(lenght)]
    # rnd_list = [2634, 6934, 7286, 3353, 4602, 3176, 3796] #для проверки, удалять цифру 3
    print(f'Этап 1-ый, список: {rnd_list}')

    num = int(input('Этап 2-ой, какую цифру ищем?: '))
    for i in range(len(rnd_list)):
        rnd_list[i] = (str(rnd_list[i])).replace(str(num), '')
    print(f'Этап 2-ой, убрали цифру: {rnd_list}')

    input('Жмите Enter для перехода к 3-у этапу')
    print(f'Этап 3-ий, складываем:')
    new_list = [rnd_list[i] for i in range(len(rnd_list))]

    for i in range(len(new_list)):
        for k in range(len(new_list[i])):
            new_list[i] = str(int(new_list[i]) // 10 + int(new_list[i]) % 10)

    for i in range(len(rnd_list)):
        print(f'{rnd_list[i]} ->', end=' ')
        print(*rnd_list[i], sep='+', end=' ')
        print(f'= {new_list[i]}')

    print(f'Этап 3-ий, сложили: {new_list}')

    input('Жмите Enter для перехода к 4-у этапу')
    print(f'Этап 4-ий - заключительный!')
    final_list = []
    for i in new_list:
        if not i in final_list:
            final_list.append(i)
    print(final_list)
    input('Нажмите Enter для выхода в меню')
    print()


def word_del_pattern():
    print()
    print('5. Убрать из строки слова содержащие подстроку')
    str = 'Python - один из самых популярных языков программирования в мире'
    print('Дана строка:', str)
    substr = 'ам'
    print('Убрать слова содержащие:', substr)
    id_start: int
    id_end: int
    is_find = 0
    while is_find != -1:
        is_find = str.find(substr)
        if is_find == -1:
            break
        id_start = str.rfind(' ', 0, is_find)
        id_end = str.find(' ', is_find)
        str = str.replace(str[id_start:id_end], ' ')
        str = str.replace('  ', ' ')
    print('Строка после обработки:', str)
    print('# Есть косяк с первым и последним словом строки, как решить не знаю, сил моих больше нету..')
    input('Нажмите Enter для выхода в меню')
    print()


def from_lecture():
    print()
    def substr_in_str_r(str, substr):
        index = str.find(substr)
        if index < 0 or index > len(str):
            return 0
        return 1 + substr_in_str_r(str[index + len(substr):], substr)

    def substr_in_str_c(str, substr):
        count = 0
        i = 0
        while i < len(str):
            i = str.find(substr, i)
            if i == -1:
                break
            count += 1
            i += len(substr)
        return count

    print('6. Задайте две строки, а программа - определит количество вхождений одной строки в другой.\n' +
          '# Для случаев поиска в строке "aaaaaa" подстроки "aa" насчитает 3, а не 5')
    str1 = input("Введите первую строку: ").strip()
    str2 = input("Введите вторую строку: ").strip()

    if len(str1) > len(str2):
        print(
            f'Строка 1 длиннее, кол-во вхождений 2-ой в 1-ую: {substr_in_str_r(str1, str2)} (рекурсия), {substr_in_str_c(str1, str2)}(цикл)')
    elif len(str1) < len(str2):
        print(
            f'Строка 2 длиннее, кол-во вхождений 1-ой во 2-ую: {substr_in_str_r(str2, str1)} (рекурсия), {substr_in_str_c(str2, str1)}(цикл)')
    elif len(str1) == len(str2):
        print(f'Строки одинаковые по длине, кол-во вхождений: {substr_in_str_r(str1, str2)}')
    input('Нажмите Enter для выхода в меню')
    print()


# program start
while True:
    print('Домашнее задание к уроку 2:\n',
          '1. Сумма цифр вещественного числа.\n',
          '2. Список из n чисел последовательности (1 + 1/n)^n.\n',
          '3. Алгоритм перемешивания списка.\n',
          '4. Программа 4 этапов.\n',
          '5. Программма удаляющая слова из строки по шаблону.\n',
          '6. Задание с лекции.\n',
          '0: Завершить работу программы.')
    number_task = int(input('Введите номер задания или 0 для выхода и жмите Enter: '))
    if number_task == 0:
        exit()
    elif number_task == 1:
        numbers_sum();
    elif number_task == 2:
        sequence_list();
    elif number_task == 3:
        shuffle_list();
    elif number_task == 4:
        four_stages();
    elif number_task == 5:
        word_del_pattern();
    elif number_task == 6:
        from_lecture();

