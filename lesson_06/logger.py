from datetime import datetime as dt

def log_step(equation, result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write(f'Кнопочный ввод;{time};{equation};{result}\n')

def log_equation(equation, result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a', encoding='UTF-8') as file:
        file.write(f'Строчный ввод;{time};{equation};{result}\n')