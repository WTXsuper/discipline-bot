import logging

from aiogram import Bot, Dispatcher, executor, types


def getToken() -> str:
    with open("API_TOKEN.txt", "r") as F:
        return F.read()


def start():
    # Configure logging (из Quick Start Aiogram Docs)
    logging.basicConfig(level=logging.INFO)

    # устаналиваем API_TOKEN
    api_token = getToken()

    # инициализируем бота
    try:
        bot = Bot(token=api_token)
        dp = Dispatcher(bot)
        logging.info("Успешная инициализация бота с API: " + api_token)
    except:
        print("ОШИБКА! Не удалось инициализировать бота!")
        exit(1)

    # Перехватываем команды /start и /help
    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        await message.answer('Привет! Я бот-помощник по дисциплине "Основы профессиональной деятельности".\n' \
                             + 'Моя задача - помочь студенту с поиском информации о текущей успеваемости и рейтинге.')
        logging.info("Сработал ответ на /start и /help")

    # TO-DO

    # запуск long pulling
    executor.start_polling(dp, skip_updates=True)
