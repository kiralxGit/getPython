equation = ''
first_number = 0
second_number = 0
operation = ''
string_equation = ''
result = 0
op_pr = {'*': 2, '/': 2, '+': 1, '-': 1} # приоритет операций

def set_equation(value):
    global equation
    if value.startswith('-'):  # так обрулил первое отрицательное
        value = value.replace('-', '0-', 1)
    equation = value

def set_first(value):
    global first_number
    first_number = value

def set_second(value):
    global second_number
    second_number = value

def set_operation(value):
    global operation
    operation = value

def set_string_equation(value):
    global string_equation
    string_equation += str(value)

def get_equation():
    global equation
    return equation

def get_string_equation():
    global string_equation
    return string_equation

def get_first():
    global first_number
    return first_number

def get_second():
    global second_number
    return second_number

def get_result():
    global result
    return result

def get_operation():
    global operation
    return operation

def additional():
    global first_number
    global second_number
    global result
    result = first_number + second_number

def difference():
    global first_number
    global second_number
    global result
    result = first_number - second_number

def multiplication():
    global first_number
    global second_number
    global result
    result = first_number * second_number

def division():
    global first_number
    global second_number
    global result
    result = round(first_number / second_number, 3)
    if result == int(result):
        result = int(result)

def replace_operand(item: str) -> str: # добавляем пробелы операндам
    match item:
        case '*':
            return ' * '
        case '/':
            return ' / '
        case '+':
            return ' + '
        case '-':
            return ' - '
        case '(':
            return ' ( '
        case ')':
            return ' ) '
        case _:
            return item

def compute_stack(equation_l: list): #производим вычисление в стэке (вроде так называется)
    global result
    nums_l = []
    opers_l = []

    def operations():
        if len(nums_l) > 1 and len(opers_l) > 0:
            b = int(nums_l.pop())
            a = int(nums_l.pop())
            temp = 0
            match opers_l.pop():
                case '*':
                    temp = a * b
                case '/':
                    temp = a / b
                case '+':
                    temp = a + b
                case '-':
                    temp = a - b
            nums_l.append(temp)

    for i in range(len(equation_l)):
        if i == len(equation_l) - 1:
            nums_l.append(equation_l[i])
            while len(nums_l) > 1:
                operations()

        elif equation_l[i] in ['(', ')']:
            if equation_l[i] == '(':
                opers_l.append('(')
            elif equation_l[i] == ')':
                while opers_l[-1] != '(':
                    operations()
                opers_l.pop()

        elif equation_l[i] in op_pr:
            if len(opers_l) == 0:
                opers_l.append(equation_l[i])
            elif opers_l[-1] == '(':
                opers_l.append(equation_l[i])
            else:
                while len(opers_l) > 0 and op_pr[opers_l[-1]] >= op_pr[equation_l[i]]:
                    operations()
                opers_l.append(equation_l[i])
        else:
            nums_l.append(equation_l[i])

    result = nums_l[0]


def calculation_equation():
    global equation
    equation_list = ''.join(map(replace_operand, equation)).split()
    compute_stack(equation_list)
