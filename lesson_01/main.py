import math

def day_of_the_week():
    print(
        '1. Программа, принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.',
        'Пример:\n',
        '6 -> да\n',
        '7 -> да\n',
        '1 -> нет',
    )
    while True:
        day = int(input('Введите цифру дня недели (1-7): '))
        if 1 <= day <= 7:
            if day == 6 or day == 7:
                print('Да, это выходной')
                break
            else:
                print('Нет, это будний день')
                break
    print('---')

def truth_check():
    print(
        '1. Напишите программу для проверки истинности утверждения\n',
        '¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z\n',
        'для всех значений предикат.')
    matrix = [[False for j in range(3)] for i in range(2 ** 3)]
    i = 0
    for x in range(2):
        for y in range(2):
            for z in range(2):
                matrix[i] = [bool(x), bool(y), bool(z)]
                i += 1

    check_true = True
    for i in matrix:
        if not(not(i[0] or i[1] or i[2]) == (not(i[0]) and not(i[1]) and not(i[2]))):
            print('Утверждение не верно!')
            check_true = False
            break
    if check_true:
        print('Утверждение верно!')

    print('---\n',
          'Есть ощущения, что где-то здесь я перемудрил :-/\n' +
          '---')

def quarter_number():
    print('3. Программа, принимает на вход координаты точки (X и Y),',
          'причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,',
          'в которой находится эта точка (или на какой оси она находится).',
          'Пример:\n',
          'x=34; y=-30 -> 4\n',
          'x=2; y=4 -> 1\n',
          'x=-34; y=-30 -> 3',
          )
    while True:
        x = int(input('Введите целое число X ='))
        y = int(input('Введите целое число Y ='))
        if x != 0 and y != 0:
            if x > 0 and y > 0:
                print('Это 1-ая четверть плоскости')
                break
            elif x < 0 and y > 0:
                print('Это 2-ая четверть плоскости')
                break
            elif x < 0 and y < 0:
                print('Это 3-ая четверть плоскости')
                break
            elif x > 0 and y < 0:
                print('Это 4-ая четверть плоскости')
                break
    print('---')

def quarter_range():
    print('4. Программа, по заданному номеру четверти, показывает',
          'диапазон возможных координат точек в этой четверти (x и y).')
    while True:
        num = int(input('Введите номер четверти (1-4):'))
        if num == 1:
            print('В текущей реализации для 1-ой четверти возможны следующие диапазоны точек:\n',
                  'X от 0 до 2 147 483 647\n',
                  'Y от 0 до 2 147 483 647')
            break
        elif num == 2:
            print('В текущей реализации для 2-ой четверти возможны следующие диапазоны точек:\n',
                  'X от 0 до -2 147 483 648\n',
                  'Y от 0 до 2 147 483 647')
            break
        elif num == 3:
            print('В текущей реализации для 3-ой четверти возможны следующие диапазоны точек:\n',
                  'X от 0 до -2 147 483 648\n',
                  'Y от 0 до -2 147 483 648')
            break
        elif num == 4:
            print('В текущей реализации для 4-ой четверти возможны следующие диапазоны точек:\n',
                  'X от 0 до 2 147 483 647\n',
                  'Y от 0 до -2 147 483 648')
            break
    print('---\n',
          'Хотя в python 3 всё не так однозначно с пределами int\n' +
          '---')

def distance_points_2d():
    print(
        '5. Программа, принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.',
        'Пример:\n',
        'A (3,6); B (2,1) -> 5,09\n',
        'A (7,-5); B (1,-1) -> 7,21',
    )
    while True:
        a = input('Введите координаты точки A через пробел: ').split()
        b = input('Введите координаты точки B через пробел: ').split()

        distance = math.sqrt(
                            (int(b[0]) - int(a[0]))**2 +
                            (int(b[1]) - int(a[1]))**2)
        print(f'Расстояние между точками = {distance:.2f}')
        break
    print('---\n',
          'Как получить 5.09 а не 5.10 я так и не понял\n' +
          '---')

def distance_points_3d():
    print(
        '6. Программа, принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.',
        'Пример:\n',
        'A (3,6,1); B (2,1,4) -> 5,09\n',
        'A (7,-5,-2); B (1,-1,1) -> 7,21',
    )
    while True:
        a = input('Введите координаты точки A через пробел: ').split()
        b = input('Введите координаты точки B через пробел: ').split()

        distance = math.sqrt(
                            (int(b[0]) - int(a[0]))**2 +
                            (int(b[1]) - int(a[1]))**2 +
                            (int(b[2]) - int(a[2]))**2)
        print(f'Расстояние между точками = {distance:.2f}')
        break
    print('---')

# program start
while True:
    number_task = int(input('Введите номер задания (1-6, для выхода 0) :'))
    if number_task == 0:
        exit()
    elif number_task == 1:
        day_of_the_week();
    elif number_task == 2:
        truth_check();
    elif number_task == 3:
        quarter_number();
    elif number_task == 4:
        quarter_range();
    elif number_task == 5:
        distance_points_2d();
    elif number_task == 6:
        distance_points_3d();
