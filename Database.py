import logging
import sqlite3

sqlite_connection = sqlite3.connect('data.db')  # подключение к БД SQLite
cur = sqlite_connection.cursor()  # задаём указатель БД


def getGroups() -> list:
    try:
        res = cur.execute("SELECT DISTINCT groupname FROM students")
        Groups = [i[0] for i in res.fetchall()]  # res.fetchall() возвращает кортеж, оттуда нужны только чистые строки
        logging.info("Список групп успешно получен из БД")
        return Groups
    except:
        print("ОШИБКА! Не удалось получить список групп!")
        exit(2)
