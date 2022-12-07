import random

def candy_game():
    def user_take() -> int:
        get_num = int(input(f'Осталось: {bank} конфет. Взять: '))
        while not (0 < get_num < 29 and get_num <= bank):
            get_num = int(input('Введите верное значение: '))
        return get_num
    def bot_take() -> int:
        bot_mistake = random.randint(0, 1) # иначе если бот первый, то выигрывает всегда
        if bank < 29:
            return bank
        elif bank % 29 and bot_mistake:
            return bank % 29
        return random.randint(1, 28)

    print()
    bank = 150
    print('Забравший последнее - забирает всё!\n'
          f'Есть {bank} конфет, за ход можно взять от 1 до 28 конфет.\n')
    user_move = bool(random.randint(0, 1)) # 0 - начинает комп, 1 - начинает игрок
    if user_move:
        print('Начинает пользователь')
    else:
        print('Начинает бот')

    while bank > 0:
        if user_move:
            took = user_take()
            bank = bank - took
            print(f'\tПользователь забирает {took} остаток {bank}')
            user_move = 0
        else:
            took = bot_take()
            bank = bank - took
            print(f'\tБот забирает {took} остаток {bank}')
            user_move = 1

    if user_move:
        print('Бот выиграл!')
    else:
        print('Вы выиграли!')

#--------------------------------------------------------------------
def tic_tac_toe_game():
    def print_field():
        print()
        print(f'{cells[0]} | {cells[1]} | {cells[2]}')
        print('---------')
        print(f'{cells[3]} | {cells[4]} | {cells[5]}')
        print('---------')
        print(f'{cells[6]} | {cells[7]} | {cells[8]}')
        print()

    def user_turn() -> int:
        get_num = 0
        while not(0 < get_num < 10):
            get_num = int(input('Куда ставим Х?: '))
        return get_num

    def bot_turn() -> int:
        return random.randint(1, 9)

    def is_free_cell(num:int) -> bool:
        return not(str(cells[num-1]).isdigit())

    def check_win():
        if cells[0] == cells[1] == cells[2]:
            return True
        elif cells[3] == cells[4] == cells[5]:
            return True
        elif cells[6] == cells[7] == cells[8]:
            return True
        elif cells[0] == cells[3] == cells[6]:
            return True
        elif cells[1] == cells[4] == cells[7]:
            return True
        elif cells[2] == cells[5] == cells[8]:
            return True
        elif cells[0] == cells[4] == cells[8]:
            return True
        elif cells[6] == cells[4] == cells[2]:
            return True
        return False

    print('\n Бот чисто рандомный, но, если не мешать ему, бывает выигрывает)')
    moves = 0
    cells = [i for i in range(1, 10)]
    print_field()
    user_move = bool(random.randint(0, 1)) # 0 - начинает комп, 1 - начинает игрок

    if user_move:
        print('Начинает пользователь X')
    else:
        print('Начинает бот O')

    while not(check_win()):
        if moves > 8:
            break
        elif user_move:
            turn = user_turn()
            while is_free_cell(turn):
                print('Клетка занята!')
                turn = user_turn()
            print(f'Ваш ход: {turn}')
            cells[turn - 1] = 'X'
            user_move = 0
        else:
            turn = bot_turn()
            while is_free_cell(turn):
                turn = bot_turn()
            print(f'Бот ставит О в клетку: {turn}')
            cells[turn - 1] = 'O'
            user_move = 1
        print_field()
        moves += 1

    if user_move and check_win():
        print('Бот выиграл!')
    elif check_win():
        print('Вы выиграли!')
    else:
        print('Ничья!')

#--------------------------------------------------------------------

def rle_algorithm():
    def rle_zip(in_str:str) -> str:
        res = ''
        length = len(in_str)
        i = 0
        count = 0
        while i < length :
            if i == 0:
                count +=1
                i += 1
                continue
            elif in_str[i] == in_str[i - 1] and i + 1 == length:
                count += 1
                res += f'{count}{in_str[i]}'
                i += 1
            elif in_str[i] == in_str[i - 1]:
                count += 1
                i += 1
            elif in_str[i] != in_str[i - 1] and i + 1 == length:
                res += f'{count}{in_str[i-1]}'
                count = 1
                res += f'{count}{in_str[i]}'
                i += 1
            elif in_str[i] != in_str[i - 1]:
                res += f'{count}{in_str[i-1]}'
                count = 1
                i += 1
        return res

    def rle_unzip(in_str: str) -> str:
        res = ''
        length = len(in_str)
        last_char = 0
        for i in range(length):
            if in_str[i].isalpha():
                res += int(in_str[last_char:i]) * in_str[i]
                last_char = i + 1
        return res

    print()
    with open('rle_unzip.txt', 'w') as data:
        data.write('aaaaabccccdeeeeeeeeeeeeef')
    with open('rle_unzip.txt', 'r') as data:
        string_long = data.read()

    print(f'Входящая строка: {string_long}')

    string_short = rle_zip(string_long)

    with open('rle_zip.txt', 'w') as data:
        data.write(string_short)

    print(f'Сжатая строка: {string_short}')

    with open('rle_zip.txt', 'r') as data:
        string_for_decode = data.read()
    print(f'Сжатая строка из файла: {string_for_decode}')
    print(f'Разжатая строка из файла: {rle_unzip(string_for_decode)}')

    input('Нажмите Enter для выхода в меню')
#--------------------------------------------------------------------


# start program
while True:
    number_task = int(input('\n1 Сыграть в конфеты\n2 Сыграть в крестики нолики\n3 RLE алгоритм\n0 для выхода\nВыбираю:'))
    if number_task == 0:
        exit()
    elif number_task == 1:
        candy_game()
    elif number_task == 2:
        tic_tac_toe_game();
    elif number_task == 3:
        rle_algorithm()