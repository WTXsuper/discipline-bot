import logging
import sqlite3


def getGroups() -> list:
    try:
        sqlite_connection = sqlite3.connect('data.db')  # подключение к БД SQLite
        cur = sqlite_connection.cursor()  # задаём указатель БД
        Groups = [i[0] for i in cur.fetchall()]  # cur.fetchall() возвращает кортеж, оттуда нужны только чистые строки
        logging.info("Список групп успешно получен из БД")
        return Groups
    except:
        print("ОШИБКА! Не удалось получить список групп!")
        exit(2)
