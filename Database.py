import logging
import sqlite3


def getGroups() -> list:
    try:
        sqlite_connection = sqlite3.connect('data.db')
        cur = sqlite_connection.cursor()
        cur.execute("SELECT DISTINCT groupname FROM students")
        Groups = [i[0] for i in cur.fetchall()]  # cur.fetchall() возвращает кортеж, оттуда нужны только чистые строки
        logging.info("Список групп успешно получен из БД")
        return Groups
    except:
        print("ОШИБКА! Не удалось получить список групп!")
        exit(2)
