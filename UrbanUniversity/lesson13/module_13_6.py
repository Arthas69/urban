from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           KeyboardButton, InlineKeyboardButton)

from settings import API_KEY


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Инфо')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)


inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы рассчета', callback_data='formulas')]
    ],
    row_width=1
)

async def calc_calories(age, growth, weight):
    return weight * 10 + 6.25 * growth - 5 * age + 5


bot = Bot(token=API_KEY)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer('Выберите вариант', reply_markup=reply_keyboard)

@dp.message_handler(Text('Рассчитать', ignore_case=True))
async def main_menu(message: types.Message):
    await message.answer('Выберите вариант:', reply_markup=inline_keyboard)

@dp.message_handler(Text('Инфо', ignore_case=True))
async def info(message: types.Message):
    await message.answer('Информация о боте!')

@dp.callback_query_handler(Text('calories'))
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()

@dp.callback_query_handler(Text('formulas'))
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Ниже формула рассчета базальной скорости метаболизма(BMR):\n\n \
                              BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (годы) + 5\n\n")
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    try:
        await state.update_data(age=int(message.text))
    except ValueError:
        await message.answer('Введите корректный возраст!')
        return 
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    try:
        await state.update_data(growth=int(message.text))
    except ValueError:
        await message.answer('Введите корректный рост!')
        return
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    try:
        await state.update_data(weight=int(message.text))
    except ValueError:
        await message.answer('Введите корректный вес!')
        return
    data = await state.get_data()
    result = await calc_calories(**data)
    await message.answer(f'Ваша норма каллорий {round(result, 2)}')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
