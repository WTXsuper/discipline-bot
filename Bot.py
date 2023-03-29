import logging
import Database as DB
from aiogram import Bot, Dispatcher, types


def getToken() -> str:
    with open("API_TOKEN.txt", "r") as F:
        return F.read()


# Настраиваем уровень логгирования (из Quick Start Aiogram Docs)
logging.basicConfig(level=logging.INFO)

# Получаем список групп из БД
Groups = DB.getGroups()

# устанавливаем API_TOKEN
API_TOKEN = getToken()

# инициализируем бота
try:
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)
    logging.info("Успешная инициализация бота с API:" + API_TOKEN)
except:
    print("ОШИБКА! Не удалось инициализировать бота!")
    exit(1)


# перехватываем команду /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('Привет! Я бот-помощник по дисциплине «Основы профессиональной деятельности»')
    logging.info("Ответ на /start")
