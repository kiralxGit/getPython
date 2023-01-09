from random import randint
from bot import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class GameStorage(StatesGroup):
    game_started = State()
    user_figure = State()
    bot_figure = State()
    cells = State()
    free_cells = State()
    user_move = State()
    check = State()



kb_x_or_o = InlineKeyboardMarkup(row_width=2).row(
    InlineKeyboardButton(text='X', callback_data='user_X'),
    InlineKeyboardButton(text='O', callback_data='user_O'))


HELP_TEXT = '\n<b>/help</b> - <i>показать список команд</i>' \
            '\n<b>/play</b> - <i>играть в крестики нолики</i>' \
            '\n<b>/end</b> - <i>закончить игру</i>'


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.answer(f'Оу, привет, {message.from_user.first_name}!')
    await help(message)


@dp.message_handler(commands=['play'])
async def start_game_3t(message: types.Message, state: FSMContext):
    await state.finish()
    async with state.proxy() as data:
        data['game_started'] = True
        data['cells'] = [' ' for i in range(1, 10)]

    await message.answer(f'Креститки нолики\n'
                         f'Первыми всегда ходят X\n'
                         f'Выбери чем хочешь ходить ты!',
                         reply_markup=kb_x_or_o)



@dp.callback_query_handler(Text(startswith='user_'))
async def user_figure(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete_reply_markup()
    if (await state.get_data()).get('game_started') == None:
        await callback.message.answer('Вначале нажми /play\n/help - помощь по командам')
        return
    if (await state.get_data()).get('user_figure'):
        await callback.answer(f'Вы уже выбрали {(await state.get_data()).get("user_figure")}! '
                              f'Для нового выбора начните игру заново')
        return
    else:
        temp = callback.data[-1]
        if temp == 'X':
            async with state.proxy() as data:
                data['user_move'] = 1
                data['user_figure'] = 'X'
                data['bot_figure'] = 'O'
        else:
            async with state.proxy() as data:
                data['user_move'] = 0
                data['user_figure'] = 'O'
                data['bot_figure'] = 'X'
            await get_bot_take(callback, state)
    await callback.message.answer(f'Вы выбрали {temp}!')

    await callback.message.answer('Играем!', reply_markup=await get_keybord(state))
    if (await state.get_data()).get('user_move') == 0:
        await get_bot_take(callback, state)


@dp.callback_query_handler(Text(startswith='take_'))
async def get_user_take(callback: types.CallbackQuery, state: FSMContext):
    if (await state.get_data()).get('game_started') is None:
        await callback.message.answer('Вначале нажми /play\n/help - помощь по командам')
        return
    temp = int(callback.data[-1])
    if (await state.get_data()).get('cells')[temp - 1] != ' ':
        await callback.answer('Клетка занята!')
    else:
        await set_state(state, (await state.get_data()).get('user_figure'), 'cells', temp - 1)
        await state.update_data(user_move=0)
        await callback.message.edit_reply_markup(reply_markup=await get_keybord(state))
        await callback.answer()
        await check_win_3t(callback, state)
        await get_bot_take(callback, state)
        await callback.message.edit_reply_markup(reply_markup=await get_keybord(state))
        await check_win_3t(callback, state)


async def set_state(state: FSMContext, value_state, name_state, key_state=0):
    async with state.proxy() as data:
        data[name_state][key_state] = value_state


async def get_keybord(state: FSMContext):
    if (await state.get_data()).get('game_started') != None:
        async with state.proxy() as data:
            kb_cells_temp = InlineKeyboardMarkup()
            for i in range(len(data['cells'])):
                kb_cells_temp.insert(InlineKeyboardButton(text=data['cells'][i], callback_data=f'take_{i + 1}'))
            return kb_cells_temp



async def get_bot_take(callback: types.CallbackQuery, state: FSMContext):
    list_cells = (await state.get_data()).get('cells')
    free_cells_list = []
    if list_cells:
        if ' ' not in list_cells:
            await check_win_3t(callback, state)
            return
    if list_cells:
        free_cells_list = list(i for i in range(len(list_cells)) if (list_cells[i] == ' '))
    if free_cells_list:
        temp = free_cells_list[randint(0, len(free_cells_list) - 1)]
        async with state.proxy() as data:
            data['cells'][temp] = data.get('bot_figure')
            data['user_move'] = 1


async def check_win_3t(callback: types.CallbackQuery, state: FSMContext):
    winning_combinations = [[0, 1, 2],
                            [3, 4, 5],
                            [6, 7, 8],
                            [0, 3, 6],
                            [1, 4, 7],
                            [2, 5, 8],
                            [0, 4, 8],
                            [6, 4, 2]]
    cells = (await state.get_data()).get('cells')
    if cells:
        for item in winning_combinations:
            if cells[item[0]] == cells[item[1]] == cells[item[2]] and cells[item[0]] != ' ':
                await end_game(callback.message, state, win=True)
            elif ' ' not in cells:
                await end_game(callback.message, state)


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'\nТебе доступны следующие команды: {HELP_TEXT}')


@dp.message_handler(commands=['end'], state="*")
async def end_game(message: types.Message, state: FSMContext, win=False):
    async with state.proxy() as data:
        if data.get('cells', None) is None:
            await message.answer('Игра не запущена!')
            return

        if win == True:
            if data.get('user_move'):
                await message.answer('БОТ ВЫИГРАЛ!')
            else:
                await message.answer('ВЫ ВЫИГРАЛИ!')
        elif win == False:
            await message.answer('НИЧЬЯ')

    await state.finish()
    await message.answer(f'Игра закончена!\nИграть ещё /play')



@dp.message_handler()
async def another_message(message: types.Message):
    await message.answer(f'<b>{message.text}</b> не понятно мне, точнее будь!\nБыть может /help тебе поможет')
