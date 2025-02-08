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

@dp.message(Command("start"))
@dp.message(F.text.lower() == "смена языка")
@dp.message(F.text.lower() == "language change")
async def change_languaege(message: Message):

    kb = [
        [
            KeyboardButton(text="Русский"),
            KeyboardButton(text="English")
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Select a language / Выберите язык "
    )

    await message.answer("Select a language / Выберите язык",
                         reply_markup=keyboard)

@dp.message(F.text.lower() == "english")
@dp.message(F.text.lower() == "menu")
async def meny(message: Message):

    kb = [
        [KeyboardButton(text="Quests"), KeyboardButton(text="Reference")],
        [KeyboardButton(text="Information for first-year students")],
        [KeyboardButton(text="Motivating Words (AI)"), KeyboardButton(text="Language change")]
        ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )

    await message.answer("Dear first-year student our bot will help you start your studies with pleasure",
                         reply_markup=keyboard)

@dp.message(F.text.lower() == "русский")
@dp.message(F.text.lower() == "меню")
async def meny(message: Message):

    kb = [
            [KeyboardButton(text="Квесты"), KeyboardButton(text="Справка")],
            [KeyboardButton(text="Информация для первокурсников")],
            [KeyboardButton(text="Мотивирующие слова (ИИ)"), KeyboardButton(text="Смена языка")]
         ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    await message.answer("Уважаемый первокурсник, наш бот Стокурсник поможет начать свое обучение с удовольствием",
                         reply_markup=keyboard)


@dp.message(F.text.lower() == "квесты")
async def place(message: Message):
    await message.answer("Выберите квест", reply_markup=ReplyKeyboardRemove())
    kb = [

            [KeyboardButton(text="Квест №1"), KeyboardButton(text="Квест №2"), KeyboardButton(text="Квест №3")],
            [KeyboardButton(text="Квест №4"), KeyboardButton(text="Квест №5")],
            [KeyboardButton(text="Меню")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    await message.answer("Или вернитесь обратно в меню", reply_markup=keyboard)

@dp.message(F.text.lower() == "quests")
async def place(message: Message):
    await message.answer("Choose a quest", reply_markup=ReplyKeyboardRemove())
    kb = [

            [KeyboardButton(text="Quest №1"), KeyboardButton(text="Quest №2"), KeyboardButton(text="Quest №3")],
            [KeyboardButton(text="Quest №4"), KeyboardButton(text="Quest №5")],
            [KeyboardButton(text="Menu")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    await message.answer("Or go to the menu", reply_markup=keyboard)

@dp.message(F.text.lower() == "справка")
async def anotation(message: Message):
    await message.answer(" Здесь будут все ссылки на источники информации, использованые для заполнения бота", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Меню"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Нажмите кнопку 'Меню' чтобы вернуться обратно", reply_markup=keyboard)

@dp.message(F.text.lower() == "reference")
async def anotation(message: Message):
    await message.answer("Here you will find all the links to the information sources used to fill out the bot.", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Menu"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Press the 'Menu' button to go back", reply_markup=keyboard)

@dp.message(F.text.lower() == "информация для первокурсников")
@dp.message(F.text.lower() == "другая категория")
async def info(message: Message):
    await message.answer("Выберите категорию", reply_markup=ReplyKeyboardRemove())
    kb = [

            [KeyboardButton(text="Транспорт"), KeyboardButton(text="Культурные места")],
            [KeyboardButton(text="Интересные заведения")],
            [KeyboardButton(text="Опасные районы"), KeyboardButton(text="Меню")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Посмотрите каждую категорию, они все помогут вам освоиться на новом месте", reply_markup=keyboard)

@dp.message(F.text.lower() == "information for first-year students")
@dp.message(F.text.lower() == "another category")
async def info(message: Message):
    await message.answer("Select a category", reply_markup=ReplyKeyboardRemove())
    kb = [

            [KeyboardButton(text="Transport"), KeyboardButton(text="Cultural places")],
            [KeyboardButton(text="Interesting places")],
            [KeyboardButton(text="Dangerous areas"), KeyboardButton(text="Menu")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Check out each category, they will help you get comfortable in a new place", reply_markup=keyboard)

@dp.message(F.text.lower() == "получить ещё больше мотивации")
@dp.message(F.text.lower() == "мотивирующие слова (ии)")
async def motivation(message: Message):
    await message.answer("Подождите", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Получить ещё больше мотивации"),
            KeyboardButton(text="Меню"),
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

    system_prompt = 'напиши мотивирующие слова для первокурсника'


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

    await message.answer("Выберите другую категорию или вернитесь в меню", reply_markup=keyboard)@dp.message(F.text.lower() == "получить ещё больше мотивации")

@dp.message(F.text.lower() == "get even more motivation")
@dp.message(F.text.lower() == "motivating words (ai)")
async def motivation(message: Message):
    await message.answer("Wait a bit", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Get even more motivation"),
            KeyboardButton(text="Menu"),
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

    system_prompt = 'напиши мотивирующие слова для первокурсника на английском языке'


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

    await message.answer("Select another category or go to the menu.", reply_markup=keyboard)

@dp.message(F.text.lower() == "транспорт")
async def metro(message: Message):
    await message.answer("'текст про то как оринтироваться в метро и тд'", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Другая категория"),
            KeyboardButton(text="Меню"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Выберите другую категорию или вернитесь в меню", reply_markup=keyboard)

@dp.message(F.text.lower() == "transport")
async def metro(message: Message):
    await message.answer("'текст про то как ориентироваться в метро и тд'", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Another category"),
            KeyboardButton(text="Menu"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Select another category or go to the menu", reply_markup=keyboard)

@dp.message(F.text.lower() == "культурные места")
async def culture(message: Message):
    await message.answer("'текст про различные культурные места в москве'", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Другая категория"),
            KeyboardButton(text="Меню"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Выберите другую категорию или вернитесь в меню", reply_markup=keyboard)

@dp.message(F.text.lower() == "cultural places")
async def culture(message: Message):
    await message.answer("'текст про различные культурные места в москве'", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Another category"),
            KeyboardButton(text="Menu"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Select another category or go to the menu", reply_markup=keyboard)

@dp.message(F.text.lower() == "интересные заведения")
async def cafe(message: Message):
    await message.answer("'текст про различные кафе и рестораны в москве'", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Другая категория"),
            KeyboardButton(text="Меню"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Выберите другую категорию или вернитесь в меню", reply_markup=keyboard)

@dp.message(F.text.lower() == "interesting places")
async def cafe(message: Message):
    await message.answer("'текст про различные кафе и рестораны в москве'", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Another category"),
            KeyboardButton(text="Menu"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Select another category or go to the menu", reply_markup=keyboard)

@dp.message(F.text.lower() == "опасные районы")
async def adangeros(message: Message):
    await message.answer("'текст про опасные районы в москве'", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Другая категория"),
            KeyboardButton(text="Меню"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Выберите другую категорию или вернитесь в меню", reply_markup=keyboard)

@dp.message(F.text.lower() == "dangerous areas")
async def adangeros(message: Message):
    await message.answer("'текст про опасные районы в москве'", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Another category"),
            KeyboardButton(text="Menu"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Select another category or go to the menu", reply_markup=keyboard)

@dp.message(F.text.lower() == "выполнено")
async def final(message: Message):
    await message.answer("Вы молодец! Продолжайте в том же духе", reply_markup=ReplyKeyboardRemove())
    kb = [

        [KeyboardButton(text="Квест №1"), KeyboardButton(text="Квест №2"), KeyboardButton(text="Квест №3")],
        [KeyboardButton(text="Квест №4"), KeyboardButton(text="Квест №5")],
        [KeyboardButton(text="Меню")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите квест"
    )

    await message.answer("Выберите следующий квест или вернитесь в меню", reply_markup=keyboard)

@dp.message(F.text.lower() == "done")
async def final(message: Message):
    await message.answer("You did well! Keep up the good work", reply_markup=ReplyKeyboardRemove())
    kb = [

        [KeyboardButton(text="Quest №1"), KeyboardButton(text="Quest №2"), KeyboardButton(text="Quest №3")],
        [KeyboardButton(text="Quest №4"), KeyboardButton(text="Quest №5")],
        [KeyboardButton(text="Menu")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    await message.answer("Select the next quest or go back to the menu.", reply_markup=keyboard)

@dp.message(F.text.lower() == "квест №1")
async def day_1(message: Message):
    await message.answer("Зайти в чат с однокурсниками", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Выполнено"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Кликните 'Выполнено' для выполнения квеста", reply_markup=keyboard)

@dp.message(F.text.lower() == "quest №1")
async def day_1(message: Message):
    await message.answer("Go into a chat with classmates", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Done"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Click 'Done' to do the task", reply_markup=keyboard)

@dp.message(F.text.lower() == "квест №2")
async def day_2(message: Message):
    await message.answer("Начать общение с однокурсниками в чате", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Выполнено"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Кликните 'Выполнено' для выполнения квеста", reply_markup=keyboard)

@dp.message(F.text.lower() == "quest №2")
async def day_1(message: Message):
    await message.answer("Write a message in a chat with classmates in order to establish contact", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Done"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Click 'Done' to do the task", reply_markup=keyboard)

@dp.message(F.text.lower() == "квест №3")
async def day_3(message: Message):
    await message.answer("Погулять с однокурсниками", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Выполнено"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Кликните 'Выполнено' для выполнения квеста", reply_markup=keyboard)

@dp.message(F.text.lower() == "quest №3")
async def day_1(message: Message):
    await message.answer("Go for a walk with classmates", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Done"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Click 'Done' to do the task", reply_markup=keyboard)

@dp.message(F.text.lower() == "квест №4")
async def day_4(message: Message):
    await message.answer("Познакомиться с ректорами", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Выполнено"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Кликните 'Выполнено' для выполнения квеста", reply_markup=keyboard)

@dp.message(F.text.lower() == "quest №4")
async def day_1(message: Message):
    await message.answer("Get acquainted with the rectors", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Done"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Click 'Done' to do the task", reply_markup=keyboard)

@dp.message(F.text.lower() == "квест №5")
async def day_5(message: Message):
    await message.answer("Выпить кофе", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Выполнено"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Кликните 'Выполнено' для выполнения квеста", reply_markup=keyboard)

@dp.message(F.text.lower() == "quest №5")
async def day_1(message: Message):
    await message.answer("Drink coffee", reply_markup=ReplyKeyboardRemove())
    kb = [
        [
            KeyboardButton(text="Done"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Click 'Done' to do the task", reply_markup=keyboard)

load_dotenv()

async def main() -> None:
    load_dotenv()
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")




    bot = Bot(token=bot_token)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())