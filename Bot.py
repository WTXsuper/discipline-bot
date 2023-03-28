import logging

from aiogram import Bot, Dispatcher, executor, types


def start():
    # Configure logging (из Quick Start Aiogram Docs)
    logging.basicConfig(level=logging.INFO)

    # устаналиваем API_TOKEN
    api_token = getToken()

    # инициализируем бота
    try:
        bot = Bot(token=api_token)
        dp = Dispatcher(bot)
    except:
        print("ОШИБКА! Не удалось инициализировать бота!")
        exit(1)
    logging.info("Успешная инициализация бота с API: " + api_token)


def getToken() -> str:
    with open("API_TOKEN.txt", "r") as F:
        return F.read()
