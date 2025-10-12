import telebot
import random
import os

r = os.listdir('images')
b = os.listdir('images_author')
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("8116606195:AAHKtzwSuBPqD25Cj7H3iDClfzLm-KUh8oE")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

#доп
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Вот список команд:/heh./help./hello./start./password./emodji./coin./mem_tt./mem_author!') 

#пароль
from bot_logic import gen_pass,gen_emodji, flip_coin  
@bot.message_handler(commands=['password'])
def send_welcome(message):
    bot.reply_to(message,gen_pass(10))

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(commands=['mem_tt'])
def send_mem(message):
    h = random.choice(r)
    with open(f'images/{h}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['mem_author'])
def send_mem(message):
    g = random.choice(b)
    with open(f'images/{g}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  


# Запуск бота
bot.polling()



