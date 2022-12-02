# Задача 2. Добавьте боту модуль, который позволяет считывать из файла вопрос, 
# отвечать на него и отправлять ответ обратно пользователю.

import telebot
import io
from telebot import types

bot = telebot.TeleBot("", parse_mode=None)

start = False

markup = types.ReplyKeyboardMarkup()
itembtn1 = types.KeyboardButton("вопрос")
markup.add(itembtn1)

@bot.message_handler(commands=["start", "help", "hello"])
def send_welcome(message):
    bot.reply_to(message, "привет, " + message.from_user.first_name, reply_markup=markup)

@bot.message_handler(content_types = ["text"])
def appeal(message):
    global start
    data = open("quest.txt", "r", encoding = "utf-8")
    answer = open("answer.txt", "r", encoding = "utf-8")
    # lines = data.read()
    # lines2 = input().split()
    # print(lines2)
    # for i in range(len(lines2)):
    #     print(lines2[i])
    
    if start:
        # try:
        
            lines = data.readline()
            if message.text in lines:
                bot.send_message(message.from_user.id, f"Ответ на твой вопрос - ")
                start = False
            else:
                bot.send_message(message.from_user.id, "Такого вопроса нет у меня!")
                start = False
                
            # if message.text in lines:
            #     bot.send_message(message.from_user.id, f"Ответ на твой вопрос - ")
            #     start = False
            # else:
            #     bot.send_message(message.from_user.id, "Такого вопроса нет у меня!")
            #     start = False

        # # except io.UnsupportedOperation:
        #     bot.send_message(message.from_user.id, "Такой вопрос есть у меня!")
        #     start = False
    data.close()
    answer.close()


    if message.text == "вопрос":
        start = True
        bot.reply_to(message, f"Введи свой вопрос!")



bot.infinity_polling()