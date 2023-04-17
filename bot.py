import logging
import database as db
from aiogram import Bot, Dispatcher, types


def readToken() -> str:
    with open("API_TOKEN.txt", "r") as F:
        return F.read()


# настраиваем уровень логгирования
logging.basicConfig(level=logging.INFO)

# устанавливаем API_TOKEN
API_TOKEN = readToken()

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
    groups = db.getGroups()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*groups)
    await message.answer('Пожалуйста, выберите группу:', reply_markup=keyboard)
    logging.info("Ответ на /start")


# перехватываем команду /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот-помощник по дисциплине «Основы профессиональной деятельности»')
    groups = db.getGroups()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*groups)
    await message.answer('Пожалуйста, выберите группу:', reply_markup=keyboard)
    logging.info("Ответ на /start")


group_choose = ""  # глобальная перемена для уточнения группы для "отлавливания"


@dp.message_handler(lambda message: message.text in db.getGroups())
async def sendStudents(message: types.Message):
    students = db.getStudents(message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*students)
    await message.answer('Пожалуйста, выберите студента:', reply_markup=keyboard)
    global group_choose
    group_choose = message.text
    logging.info("Выбрана группа {}, выведен список студентов".format(group_choose))


@dp.message_handler(lambda message: message.text in db.getStudents(group_choose))
async def sendStudents(message: types.Message):
    student_info = db.getRating(message.text)
    answer_str = "<i>{}</i>\n" \
                 "Посещаемость: <b>{}%</b>\n" \
                 "Был на <b>{}</b> занятиях из <b>{}</b>\n" \
                 "Рейтинг: <b>{}</b>".format(message.text, (int(100 * student_info['attendance'])),
                                             student_info['attended'], student_info['lesson_count'],
                                             student_info['rating'])
    await message.answer(answer_str, parse_mode=types.ParseMode.HTML, reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Вы можете воспользоваться командой /start для повторного поиска")
    logging.info("Выведена информация о студенте {}".format(message.text))
