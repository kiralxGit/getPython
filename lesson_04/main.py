from random import randint as ri

def gen_equation(coef): # собираем уравнение из коэффициентов
    parts = []
    for i in reversed(range(0, len(coef))):
        if coef[i] != 0:
            if coef[i] == 1:
                if i == 0:
                    parts.append(f'1')
                elif i == 1:
                    parts.append(f'x')
                elif i > 1:
                    parts.append(f'x**{i}')
            elif coef[i] == -1:
                if i == 0:
                    parts.append(f'-1')
                elif i == 1:
                    parts.append(f'-x')
                elif i > 1:
                    parts.append(f'-x**{i}')
            elif coef[i] > 1 or coef[i] < 0:
                if i == 0:
                    parts.append(f'{coef[i]}')
                elif i == 1:
                    parts.append(f'{coef[i]}*x')
                elif i > 1:
                    parts.append(f'{coef[i]}*x**{i}')
    result = ''
    for i in range(len(parts)):
        if parts[i][0] == '-':
            result += parts[i]
        elif i == 0:
            result += parts[i]
        else:
            result += ' + ' + parts[i]
    result = result.replace('-', ' - ').strip() + ' = 0'
    if result.startswith('- '):
        result = result.replace('- ', '-', 1)
    return result

def save_file(eq): # сохраняем в файл
        name_file = int(input('Введите имя файла(только цифры) для записи или перезаписи: '))
        with open(f'{name_file}.txt', 'w') as data:
            data.write(eq)

def create_equation_file(): # функция первой части программы
    k = int(input('Введите степень k: '))
    coefficient = {i:ri(-100, 100) for i in range(k + 1)}
    print(f'Словарь: {coefficient}')

    equation = gen_equation(coefficient)
    print(f'Уравнение: {equation}')

    if_save_file = int(input('Введите 1 если записать выражение в файл, 0 если нет: '))
    if if_save_file == 1:
        save_file(equation)

#------------------------------------------------------------------------------------------

def parsing_to_monomials (eq): # парсим на одночлены
    for i in range(len(eq)):
        equals_id = eq[i].find('=')
        eq[i] = eq[i][:equals_id].replace(' - ', ' + -').split(' + ')

    return eq

def monomials_to_dict(mons): # разбираем одночлены на словари
    list_int = []
    for item in mons:
        dict_temp = {}
        for j in item:
            if j.find('*x**') != (-1):
                dict_temp[int(j[j.find('*x**') + 4:])] = int(j[:j.find('*x**')])
            elif j.find('-x**') != (-1):
                    dict_temp[int(j[j.find('x**') + 3:])] = -1
            elif j.find('x**') != (-1):
                    dict_temp[int(j[j.find('x**') + 3:])] = 1
            elif j.find('*x') != (-1):
                    dict_temp[1] = int(j[:j.find('*x')])
            elif j.find('x') != (-1):
                    dict_temp[1] = 0
            else:
                dict_temp[0] = int(j)
        list_int.append(dict_temp)
    return list_int

def addition_monomials(list_dicts): # складываем словари
    result = {}
    for i in list_dicts:
        for key in i:
            if result.get(key, False) == False:
                result[key] = i[key]
            else:
                result[key] += i[key]
    return result

def sum_of_equations(): # функция второй части программы
    name_files = []
    while len(name_files) < 2:
        name_files = input('Введите имена файлов через пробел: ')
        name_files = name_files.strip().split(' ')

    equations = []
    for i in range(len(name_files)):
        with open(f'{name_files[i]}.txt', 'r') as file:
            equations.append(file.read())

    print('\nПрочитали из файлов следующие уровнения:', *equations, sep='\n', end='\n\n')

    monomials = parsing_to_monomials(equations)
    print('Распарсили их на одночлены:', *monomials, sep='\n', end='\n\n')

    list_dicts_int = monomials_to_dict(monomials)
    print('Распарсили одночлены в словари:', *list_dicts_int, sep='\n', end='\n\n')

    sum_of_polynomials = addition_monomials(list_dicts_int)
    print(f'Получили сумму многочленов:\n{sum_of_polynomials}\n')

    equation = gen_equation(sum_of_polynomials)

    print(f'Уравнение: {equation}')

    if_save_file = int(input('Введите 1 если записать выражение в файл, 0 если нет: '))
    if if_save_file == 1:
        save_file(equation)

# start program

while True:
    number_task = int(input('Введите 1 для создания файла, 2 для сложения, 0 для выхода: '))
    if number_task == 0:
        exit()
    elif number_task == 1:
        create_equation_file()
    elif number_task == 2:
        sum_of_equations()
