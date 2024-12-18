from string import ascii_letters as al

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,
                           KeyboardButton, InlineKeyboardButton)

from settings import API_KEY
from crud_functions_14_5 import get_all_products, add_user, is_included


########## STATES START ###########
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


######### STATES END ##############

######### KEYBOARDS START #########
reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Инфо')],
        [KeyboardButton(text='Купить')],
        [KeyboardButton(text="Регистрация")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)

calories_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы рассчета', callback_data='formulas')]
    ],
    row_width=1
)

product_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying'),
         InlineKeyboardButton(text='Product2', callback_data='product_buying'),
         InlineKeyboardButton(text='Product3', callback_data='product_buying'),
         InlineKeyboardButton(text='Product4', callback_data='product_buying')]
    ]
)
######### KEYBOARDS END ##########


bot = Bot(token=API_KEY)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


async def calc_calories(age, growth, weight):
    return weight * 10 + 6.25 * growth - 5 * age + 5


############## HANDLERS START ####################
@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer('Выберите вариант', reply_markup=reply_keyboard)


@dp.message_handler(Text('Рассчитать', ignore_case=True))
async def main_menu(message: types.Message):
    await message.answer('Выберите вариант:', reply_markup=calories_keyboard)


@dp.message_handler(Text('Инфо', ignore_case=True))
async def info(message: types.Message):
    await message.answer('Информация о боте!', reply_markup=reply_keyboard)


@dp.message_handler(Text('Купить', ignore_case=True))
async def get_buying_list(message: types.Message):
    products = get_all_products()
    for product in products:
        with open(product[3], 'rb') as img:
            await message.answer_photo(
                img,
                caption='Название: {} | Описание: {} | Цена: {}'.format(*product[:3]),
            )
    await message.answer("выберите продукт для покупки", reply_markup=product_keyboard)


############## HANDLERS END ###############


############## USER STATE START ##################
@dp.callback_query_handler(Text('calories'))
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


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


############# USER STATE END #################


############## REGISTRATION STATE START ##############
@dp.message_handler(Text("Регистрация"))
async def sign_up(message: types.Message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    if (username := message.text) and all(i in al for i in username):
        if is_included(username):
            await message.answer('Пользователь существует, введите другое имя')
            return
        await state.update_data(username=message.text)
    else:
        await message.answer('Введите имя пользователя (только латинский алфавит):')
        return
    await message.answer('Введите свой email:')
    await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    try:
        await state.update_data(age=int(message.text))
    except ValueError:
        await message.answer("Введите корректный возраст:")
        return
    user = await state.get_data()
    add_user(**user)
    await message.answer(f' Спасибо за регистрацию, {user["username"]}',
                         reply_markup=reply_keyboard)
    await state.finish()


############## REGISTRATION STATE END ################


@dp.callback_query_handler(Text('formulas'))
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Ниже формула рассчета базальной скорости метаболизма(BMR):\n\n \
    BMR = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (годы) + 5\n\n")
    await call.answer()


@dp.callback_query_handler(Text('product_buying'))
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
