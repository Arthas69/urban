from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from settings import API_KEY


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


bot = Bot(token=API_KEY)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(Text('Calories', ignore_case=True))
async def set_age(message: types.Message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))

    data = await state.get_data()
    result = await calc_calories(**data)
    await message.answer(f'Ваша норма каллорий {round(result, 2)}')
    await state.finish()


async def calc_calories(age, growth, weight):
    return weight * 10 + 6.25 * growth - 5 * age + 5

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
