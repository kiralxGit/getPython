import view
import model
import logger

def input_first(): #проверяем что в строке, если число, то по старой схеме, если нет по новой
    while True:
        number = view.input_first_value()
        if number.isdigit():
            model.set_first(int(number))
            break
        for item in number:
            if item.isdigit() or item in ['*', '/', '+', '-', '=', '(', ')']:
                continue
            else:
                view.input_error()
                break
        else:
            model.set_equation(number)
            break

def input_second():
    while True:
        number = view.input_number()
        if model.get_operation() == '/' and number == 0:
            view.print_division_zero()
        else:
            model.set_second(number)
            break

def input_operation():
    operation = view.input_operation()
    model.set_operation(operation)

def solution():
    operand = model.get_operation()
    match operand:
        case '+':
            model.additional()
        case '-':
            model.difference()
        case '*':
            model.multiplication()
        case '/':
            model.division()
        case '=':
            return True
    result_string = f'{model.get_first()} ' \
                    f'{model.get_operation()} ' \
                    f'{model.get_second()} = ' \
                    f'{model.get_result()}'
    view.print_to_console(result_string)
    model.set_first(model.get_result())

def start():
    input_first()
    model.set_string_equation(model.get_first())
    if model.get_first() != 0:
        while True:
            input_operation()
            if model.get_operation() == '=':
                logger.log_step(model.get_string_equation(), model.get_result())
                view.log_off(model.get_result())
                break
            model.set_string_equation(model.get_operation())
            input_second()
            model.set_string_equation(model.get_second())
            print(f'строка для лога {model.get_string_equation()}')
            solution()
    elif model.get_equation() != '':
        print('введено:', model.get_equation())
        model.calculation_equation()
        logger.log_equation(model.get_equation(),model.get_result())
        view.log_off(model.get_result())


