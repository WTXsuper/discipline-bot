import logging
import sqlite3

db_logger = logging.getLogger("database")  # логгер для БД


def getGroups() -> list:
    try:
        sqlite_connection = sqlite3.connect('data.db')  # подключение к БД SQLite
        cur = sqlite_connection.cursor()  # задаём указатель БД
        cur.execute("SELECT DISTINCT groupname FROM students")
        Groups = [i[0] for i in cur.fetchall()]  # cur.fetchall() возвращает кортеж, оттуда нужны только чистые строки
        sqlite_connection.close()
        db_logger.info("Список групп успешно получен из БД:" + ",".join(Groups))
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
        sqlite_connection.close()
        db_logger.info("Список студентов группы '{}' успешно получен из БД".format(group))
        return Students
    except:
        print("ОШИБКА! Не удалось получить студентов группы '{}'!".format(group))
        exit(2)


def getRating(student: str) -> dict:
    try:
        sqlite_connection = sqlite3.connect('data.db')  # подключение к БД SQLite
        cur = sqlite_connection.cursor()  # задаём указатель БД

        # получим оценки студента, чтобы найти среднюю оценку (успеваемость)
        cur = cur.execute("SELECT * FROM rating WHERE fullname = '{}';".format(student))
        marks_tuple = cur.fetchall()  # получаем всю строку про выбранного студента

        rating = 0  # сумматор для рейтинга (кол-во баллов)
        skipped = 0  # счётчик пропущенных занятий
        lesson_count = len(marks_tuple[0]) - 1  # кол-во занятий = кол-во столбцов без учёта имени

        # Перебираем элементы, полученным из ДБ, кроме первой колонки (т.к. это имя студента)
        for i in range(lesson_count):
            element = marks_tuple[0][i + 1]
            # добавляем существующие элементы (тип не NULL (None))
            if element:
                rating += element
            else:
                skipped += 1

        attendance = (lesson_count - skipped) / lesson_count  # посещаемость (дробью)
        study_info = {'rating': rating, 'attendance': attendance, 'lesson_count': lesson_count,
                      'attended': (lesson_count - skipped)}
        sqlite_connection.close()
        db_logger.info("Информация о студенте '{}' успешна получена из БД".format(student))
        return study_info
    except:
        print("ОШИБКА! Не удалось получить информацию о студенте '{}'!".format(student))
        exit(2)
