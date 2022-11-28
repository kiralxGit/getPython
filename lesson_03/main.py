from random import randint as rnd
import decimal


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_odd_numbers():
    print()
    len_my_list = int(input('Введите кол-во элементов списка: '))
    my_list = [rnd(0, 9) for i in range(len_my_list)]
    sum = 0
    for i in range(1, len(my_list), 2):
        sum += my_list[i]
    print(f'Исходный массив {my_list},\nсумма эл-ов на нечётных индексах = {sum}')
    print()


# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]
def multiply_pair():
    print()
    my_list = input('Введите список чисел пробел: ').split()
    my_list = [int(i) for i in my_list]
    length = len(my_list)
    new_list = []
    for i in range(length - int(length / 2)):
        new_list.append(my_list[i] * my_list[-(i + 1)])
    print(f'Произведение пар чисел списка = {new_list}')
    print()


# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def max_fractional():
    print()
    length = int(input('Введите длину списка: '))
    dc = decimal.Decimal
    my_list = []
    for i in range(length):  # заполняем массив сразу decimal с округлением до 2х симв в меньшую сторону
        my_list.append(rnd(10, 99) + dc(rnd(10, 99) / 100).quantize(dc("1.00"), decimal.ROUND_DOWN))
    print('Рандомный список: [', end='')
    print(*my_list, sep=', ', end=']\n')

    my_list = [my_list[i] - my_list[i] // 1 for i in range(len(my_list))]  # отбрасывааем целое
    print('Дробные части списка:: [', end='')
    print(*my_list, sep=', ', end=']\n')

    max_id = 0
    min_id = 0
    for i in range(len(my_list)):  # ищем максимальное и минимальное
        if my_list[i] > my_list[max_id]:
            max_id = i
        elif my_list[i] < my_list[min_id]:
            min_id = i

    diff = my_list[max_id] - my_list[min_id]  # вычитаем

    print(f'Разница между max и min дробной частью = {diff}')
    print()

    print()


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def ten_to_bin():
    print()
    num10 = int(input('Введите число в десятичном формате: '))
    if (num10 == 0):
        print('В двоичном: 0')
        return
    num2 = ''
    while num10 > 0:
        num2 += str(num10 % 2)
        num10 //= 2
    print('В двоичном:', num2[::-1])
    print()


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def negofib():
    print()
    k = int(input('Введите число для Негафибоначчи: '))
    fib_list = [1, 0, 1]
    if k == 1 or k == -1:
        print(f'Последовательность для фичсла {k} -> {fib_list}')
        return
    for i in range(3, k * 2 + 1, 2):
        fib_list.append((fib_list[i - 1]) + (fib_list[i - 2]))
        fib_list.insert(0, (fib_list[1]) - (fib_list[0]))

    print(f'Список чисел Фибоначчи и Негафибоначчи:\n{fib_list}')
    print()


# program start

while True:
    number_task = int(input('Введите номер задания (1-5) или 0 для выхода и жмите Enter: '))
    if number_task == 0:
        exit()
    elif number_task == 1:
        sum_odd_numbers()
    elif number_task == 2:
        multiply_pair()
    elif number_task == 3:
        max_fractional()
    elif number_task == 4:
        ten_to_bin()
    elif number_task == 5:
        negofib()
