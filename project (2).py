import asyncio
import os


from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

dp = Dispatcher()

@dp.message(F.text.lower() == "день 1")
async def day_1(message: Message):
    await message.answer("Задание: зайти в чат с однокурсниками", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Выполнено"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Нажмите выполнено по окончании выполнения задания", reply_markup=keyboard)


@dp.message(F.text.lower() == "день 2")
async def day_2(message: Message):
    await message.answer("Задание: написать сообщение в чат с однокурсниками с целью наладить контакт", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Выполнено"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Нажмите выполнено по окончании выполнения задания", reply_markup=keyboard)


@dp.message(F.text.lower() == "день 3")
async def day_3(message: Message):
    await message.answer("Задание: погулять с однокурсниками", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Выполнено"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Нажмите выполнено по окончании выполнения задания", reply_markup=keyboard)


@dp.message(F.text.lower() == "день 4")
async def day_4(message: Message):
    await message.answer("Задание: познакомиться с ректорами", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Выполнено"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Нажмите выполнено по окончании выполнения задания", reply_markup=keyboard)


@dp.message(F.text.lower() == "день 5")
async def day_5(message: Message):
    await message.answer("Задание: выпить кофе", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Выполнено"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Нажмите выполнено по окончании выполнения задания", reply_markup=keyboard)

@dp.message(F.text.lower() == "выполнено")
async def final(message: Message):
    await message.answer("Вы молодец! Продолжайте в том же духе", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="День 1"),
            KeyboardButton(text="День 2"),
            KeyboardButton(text="День 3"),
            KeyboardButton(text="День 4"),
            KeyboardButton(text="День 5")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите день"
    )

    await message.answer("Выберите следующий день", reply_markup=keyboard)



async def start (message: Message):
    kb = [
        [
            KeyboardButton(text="Квесты"),
            KeyboardButton(text="Топ советов для быстрой адаптации")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите направление"
    )

    await message.answer("Уважаемый первокурсник, наш бот Стокурсник поможет начать свое обучение с удовольствием",
                         reply_markup=keyboard)

@dp.message(F.text.lower() == "квесты")
async def cmd_start(message: Message):
    await message.answer("Выберите", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="День 1"),
            KeyboardButton(text="День 2"),
            KeyboardButton(text="День 3"),
            KeyboardButton(text="День 4"),
            KeyboardButton(text="День 5")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите день"
    )

    await message.answer("день", reply_markup=keyboard)


load_dotenv()

async def main() -> None:
    load_dotenv()
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")


    dp.message.register(start, Command("start"))

    bot = Bot(token=bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())