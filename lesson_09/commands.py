import random
from time import sleep

from bot import dp, bot
from aiogram import types

bank = None
user_move = None

HELP_TEXT = '\n<b>/help</b> - <i>показать список команд</i>' \
            '\n<b>/play</b> - <i>играть в конфеты</i>' \
            '\n<b>/bank</b> - <i>показать остаток конфет</i>' \
            '\n<b>/end</b> - <i>закончить игру</i>'


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.delete()
    await bot.send_message(message.from_user.id, text=f'Оу, привет, {message.from_user.first_name}!')
    await help(message)


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'\nТебе доступны следующие команды: {HELP_TEXT}')


@dp.message_handler(commands=['play'])
async def start_game(message: types.Message):
    global bank
    global user_move
    if bank is None:
        bank = 150
        user_move = random.randint(0, 1)
        if user_move:
            await message.answer('Вы начинаете!')
        else:
            await message.answer('Бот начинает')
        sleep(1 / 2)
        await message.answer(f'Забравший последнее - забирает всё!\n'
                             f'На столе сейчас {bank} конфет\n')
    else:
        await message.answer(f'Игра уже запущена!\n'
                             f'На столе сейчас {bank} конфет\n')
    await game(message)


async def game(message: types.Message):
    sleep(1 / 2)
    if bank == 0:
        await finish_game(message)
    elif user_move:
        await bot.send_message(message.from_user.id,
                               text=f'Ваш ход! Остаток {bank} конфет\n'
                                    f'Можно взять от 1 до 28 конфет, но не больше чем осталось.\n')
    else:
        await bot.send_message(message.from_user.id, text='Ходит бот')
        await bot_take(message)

async def bot_take(message: types.Message):
    global bank
    global user_move
    temp = 0
    sleep(1 / 2)
    bot_mistake = random.randint(0, 1)
    if bank < 29:
        temp = bank
    elif bank % 29 and bot_mistake:
        temp = bank % 29
    else:
        temp = random.randint(1, 28)
    bank -= temp
    await message.answer(f'Бот забирает {temp}, осталось {bank} конфет')
    user_move = 1
    await game(message)

async def finish_game(message: types.Message):
    global bank
    global user_move
    if user_move:
        await bot.send_message(message.from_user.id, text='Бот выиграл!')
        await end_game(message)
    else:
        await bot.send_message(message.from_user.id, text='Вы выиграли!')
        await end_game(message)

@dp.message_handler(lambda message: message.text.isdigit() and user_move == 1)
async def user_take(message: types.Message):
    global bank
    global user_move
    temp = int(message.text)
    if 0 < temp < 29 and temp <= bank:
        bank -= temp
        await message.answer(f'Вы взяли {temp}, осталось {bank} конфет')
        user_move = 0

    else:
        await message.answer(f'Вы ввели некорректное значение!')
    await game(message)

@dp.message_handler(commands=['bank'])
async def show_bank(message: types.Message):
    global bank
    if bank is None:
        await message.answer('Игра не была запущена!')
        return
    await message.answer(f'Осталось {bank} конфет')


@dp.message_handler(commands=['end'])
async def end_game(message: types.Message):
    global bank
    global user_move
    if bank is None:
        await message.answer('Игра не была запущена!')
        return
    bank = None
    user_move = None
    await message.answer(f'Игра закончена!\nИграть ещё /play')


@dp.message_handler()
async def another_message(message: types.Message):
    await message.answer(f'<b>{message.text}</b> не понятно мне, точнее будь!\nБыть может /help тебе поможет')