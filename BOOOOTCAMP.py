import asyncio
import os
import time

import requests
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext


class UserInfo(StatesGroup):
    question = State()

dp = Dispatcher()

@dp.message(F.text.lower() == "в меню")
async def start (message: Message):
    await state.set_state(UserInfo.question)
    kb = [
        [
            KeyboardButton(text="Квесты"),
            KeyboardButton(text="Информация для первокурсников"),
            KeyboardButton(text="Справка"),
            KeyboardButton(text="Мотивирующие слова (ИИ)"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        row_wide=1,
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите направление"
    )

    await message.answer("Уважаемый первокурсник, наш бот Стокурсник поможет начать свое обучение с удовольствием",
                         reply_markup=keyboard)

@dp.message(F.text.lower() == "получить ещё больше мотивации")
@dp.message(F.text.lower() == "мотивирующие слова (ии)")
async def anotation(message: Message, data=None, state: FSMContext):


    await message.answer("подождите", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Получить ещё больше мотивации"),
            KeyboardButton(text="В меню"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )


    load_dotenv()
    folder_id = os.getenv("YANDEX_FOLDER_ID")
    api_key = os.getenv("YANDEX_API_KEY")
    gpt_model = 'yandexgpt-lite'

    system_prompt = data['question']


    body = {
        'modelUri': f'gpt://{folder_id}/{gpt_model}',
        'completionOptions': {'stream': False, 'temperature': 0.3, 'maxTokens': 2000},
        'messages': [
            {'role': 'system', 'text': system_prompt},

        ],
    }
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completionAsync'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Api-Key {api_key}'
    }

    response = requests.post(url, headers=headers, json=body)
    operation_id = response.json().get('id')

    url = f"https://llm.api.cloud.yandex.net:443/operations/{operation_id}"
    headers = {"Authorization": f"Api-Key {api_key}"}

    while True:
        response = requests.get(url, headers=headers)
        done = response.json()["done"]
        if done:
            break
        time.sleep(2)

    data = response.json()
    answer = data['response']['alternatives'][0]['message']['text']


    await message.answer(answer)

    await message.answer("выберите другую категоорию или вернитесь обратно в меню", reply_markup=keyboard)


@dp.message(F.text.lower() == "информация для первокурсников")
@dp.message(F.text.lower() == "другая категория")
async def anotation(message: Message):
    await message.answer("Выберите категорию", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Метро и автобусы"),
            KeyboardButton(text="Культурные места"),
            KeyboardButton(text="Кафе и рестораны"),
            KeyboardButton(text="Опасные районы"),
            KeyboardButton(text="В меню"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Посмотрите каждую категорию, они все помогут вам освоиться на новом месте", reply_markup=keyboard)

@dp.message(F.text.lower() == "метро и автобусы")
async def anotation(message: Message):
    await message.answer("'текст про то как оринтироваться в метро и тд'", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="другая категория"),
            KeyboardButton(text="В меню"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("выберите другую категоорию или вернитесь обратно в меню", reply_markup=keyboard)

@dp.message(F.text.lower() == "культурные места")
async def anotation(message: Message):
    await message.answer("'текст про различные культурные места в москве'", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="другая категория"),
            KeyboardButton(text="В меню"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("выберите другую категоорию или вернитесь обратно в меню", reply_markup=keyboard)

@dp.message(F.text.lower() == "кафе и рестораны")
async def anotation(message: Message):
    await message.answer("'текст про различные кафе и рестораны в москве'", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="другая категория"),
            KeyboardButton(text="В меню"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("выберите другую категоорию или вернитесь обратно в меню", reply_markup=keyboard)

@dp.message(F.text.lower() == "опасные районы")
async def anotation(message: Message):
    await message.answer("'текст про опасные районы в москве'", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="другая категория"),
            KeyboardButton(text="В меню"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("выберите другую категоорию или вернитесь обратно в меню", reply_markup=keyboard)

@dp.message(F.text.lower() == "справка")
async def anotation(message: Message):
    await message.answer("текст для жури, откда взята вся информация вставленная в бота", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="В меню"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Нажмите кнопку 'В меню' чтобы вернуться обратно", reply_markup=keyboard)




@dp.message(F.text.lower() == "квесты")
async def place(message: Message):
    await message.answer("Выберите квест", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="квест 1"),
            KeyboardButton(text="квест 2"),
            KeyboardButton(text="квест 3"),
            KeyboardButton(text="квест 4"),
            KeyboardButton(text="квест 5"),
            KeyboardButton(text="В меню")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите квест"
    )

    await message.answer("Или вернитесь обратно в меню", reply_markup=keyboard)

@dp.message(F.text.lower() == "выполнено")
async def final(message: Message):
    await message.answer("Вы молодец! Продолжайте в том же духе", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="квест 1"),
            KeyboardButton(text="квест 2"),
            KeyboardButton(text="квест 3"),
            KeyboardButton(text="квест 4"),
            KeyboardButton(text="квест 5"),
            KeyboardButton(text="В меню")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите квест"
    )

    await message.answer("Выберите следующий квест или вернитесь в меню", reply_markup=keyboard)


@dp.message(F.text.lower() == "квест 1")
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


@dp.message(F.text.lower() == "квест 2")
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


@dp.message(F.text.lower() == "квест 3")
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


@dp.message(F.text.lower() == "квест 4")
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


@dp.message(F.text.lower() == "квест 5")
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



load_dotenv()

async def main() -> None:
    load_dotenv()
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")


    dp.message.register(start, Command("start"))

    bot = Bot(token=bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())