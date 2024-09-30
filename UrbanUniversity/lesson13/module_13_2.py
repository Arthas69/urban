from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

from settings import API_KEY


bot = Bot(token=API_KEY)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message(CommandStart())
async def start(message: types.Message):
    print("Привет! Я бот помогающий твоему здоровью.")


@dp.message()
async def all_messages(message: types.Message):
    print("Введите команду /start, чтобы начать общение.")


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())
