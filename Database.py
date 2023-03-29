import logging
import sqlite3


def getGroups() -> list:
    try:
        sqlite_connection = sqlite3.connect('data.db')  # подключение к БД SQLite
        cur = sqlite_connection.cursor()  # задаём указатель БД
        cur.execute("SELECT DISTINCT groupname FROM students")
        Groups = [i[0] for i in cur.fetchall()]  # cur.fetchall() возвращает кортеж, оттуда нужны только чистые строки
        logging.info("Список групп успешно получен из БД:" + ",".join(Groups))
        return Groups
    except:
        print("ОШИБКА! Не удалось получить список групп!")
        exit(2)


def getStudents(group: str) -> list:
    try:
        sqlite_connection = sqlite3.connect('data.db')  # подключение к БД SQLite
        cur = sqlite_connection.cursor()  # задаём указатель БД
        cur = cur.execute("SELECT fullname FROM students WHERE groupname = '{}';".format(group))
        Students = [i[0] for i in cur.fetchall()]  # cur.fetchall() возвращает кортеж, оттуда нужны только чистые строки
        logging.info("Список студентов группы {} успешно получен из БД".format(group))
        return Students
    except:
        print("ОШИБКА! Не удалось получить студентов группы {}!".format(group))
        exit(2)