# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в объект DEFINITOINS на 13 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='set your token here', parse_mode='html')
# создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
    'qc': 'quality contrlo',
    'qa': 'quality assuarance',
    'tms': 'test management system',
    'istqb': 'international software testing qualifications board',
    'rps': 'requests per second',
    'ci/cd': 'continuous integration cintinuous development',
    'sdls': 'software development lige cycle',
    'crud': 'create, read, update, delete',
    'adb': 'android debug bridge',
    'dns': 'domain names system',
    'regression testing': 'a type of change-related testing to detect whether defects have been introduced or uncovered in unchanged areas of the software',
    'smoke test': 'test suite that covers the main functionality of a component or system to determine whether it works properly before planned testing begins',
    'api': 'a type of interface in which the components or systems involved exchange information in a defined formal structure',
}

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='🤓 Hi! I can help you to decipher complicated terms and abbriviations both in English and in Russian 🤓',)

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text= '😋 I do not know this term yet. Try and check it here: https://glossary.istqb.org/ 😋',)
        
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Definition:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text= '🤓 I am waiting for the next term 🤓',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
