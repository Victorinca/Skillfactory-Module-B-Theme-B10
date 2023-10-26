# Основной файл бота - конвертора валют
import telebot
from config import currencies, TOKEN
from extensions import APIException, Converter
import traceback

bot = telebot.TeleBot(TOKEN)

# Обработчик сообщений - функция, которая будет выполняться при получении определённого сообщения.
# Чтобы из обычной функции сделать обработчик сообщений для бота надо воспользоваться декоратором.
#@bot.message_handler(filters)
#def function_name(message):
#    bot.reply_to(message, "Это обработчик сообщений")

# Обработчики сообщений состоят из одного или нескольких фильтров:
# 2 основных фильтра: 1) Тип контента content_types - по умолчанию ['text'] 2) Команды commands
# Для обработчиков сообщений разрешено любое имя функции, поэтому function_name может принимать любое значение.
# Функция должна принимать не более одного аргумента, который будет сообщением, обрабатываемым функцией.
# Аргумент message имеет все поля перечисленные по ссылке:
# https://core.telegram.org/bots/api#message

# Обработчик команд start - обрабатываются все сообщения содержащие команду '/start'
@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = f"{message.chat.username},\n" \
           "Вас приветствует Бот - конвертер валют, помогающий в онлайн режиме пересчитать нужную сумму из одной валюты в другую, например, доллар в рубль.\n" \
           "Валютный калькулятор быстро и точно рассчитает соотношение актуальных курсов таких валют как: доллары США, евро, российские рубли и др.\n" \
           "Все расчёты выполняются на основе официальных данных о котировках международных валют, обновляемых ЦБ РФ ежедневно.\n" \
           "Ознакомьтесь со справкой по работе с Ботом - используйте команду /help"
    bot.send_message(message.chat.id, text)

# Обработчик команды help
@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = "Справка по работе с ботом.\n\n" \
           "Чтобы начать работу, введите данные в следущем формате:\n" \
           "<имя валюты> <в какую валюту сконвертировать> <количество первой валюты>\n\n" \
           "Пример, чтобы сконвертировать 2 доллара в рубли, введите:\n" \
           "доллар рубль 2\n\n" \
           "Для просмотра списка валют используйте команду /values'\n\n" \
           "Другие доступные команды:\n" \
           "/start - стартовое приветствие\n" \
           "/help - справка по работе с ботом"
    bot.send_message(message.chat.id, text)

# Обработчик команды values - информация о всех доступных валютах
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for currency in currencies.keys(): # пройдем по ключам списка-словаря
        text = '\n'.join((text, currency)) # каждый ключ будет написан с новой строки
    bot.send_message(message.chat.id, text)

# обработчик данных для конвертации
@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message): # Конвертация
    values = message.text.split()
    # Возможные ошибки
    try:
        if len(values) != 3:
            raise APIException('Неверное параметры или количество параметров!')

        base, quote, amount = values
        total = Converter.get_price(base, quote, amount)

    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Не удалось обработать команду - неизвестная ошибка:\n{e}")
    else:
        text = f"Цена: {amount} {base} = {total} {quote}"
        bot.send_message(message.chat.id, text)

# запуск бота
bot.polling(none_stop=True)
