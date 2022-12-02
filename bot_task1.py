# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot
import io
from telebot import types

bot = telebot.TeleBot("", parse_mode=None)

start = False

markup = types.ReplyKeyboardMarkup()
itembtn1 = types.KeyboardButton("обращение")
markup.add(itembtn1)

@bot.message_handler(commands=["start", "help", "hello"])
def send_welcome(message):
    bot.reply_to(message, "привет, " + message.from_user.first_name, reply_markup=markup)

@bot.message_handler(content_types = ["text"])
def appeal(message):
    global start
    data = open("appeal.txt", "r+", encoding = "utf-8")
    if start:
        try:
            data.writelines(message.text + "\n")
            bot.send_message(message.from_user.id, "Обращение зарегистрировано")
            start = False
        except io.UnsupportedOperation:
            data.writelines(message.text + "\n")
            bot.send_message(message.from_user.id, "Обращение зарегистрировано")
            start = False
            
    if message.text == "обращение":
        start = True
        bot.reply_to(message, f"Введи свое обращение!")
    data.close

bot.infinity_polling()