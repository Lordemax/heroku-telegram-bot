# -*- coding: utf-8 -*-
#import redis
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
bot = telebot.TeleBot["811545344:AAHwO9cyHPnSlA7a6SwZvDEtbAlj7GhcieQ"]
#api_token = os.environ['API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
#r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
# bot = telebot.TeleBot(594779131:AAGStMS5a9vcfmjjKdI9HSaxjHq4SsKhRnw)
# some_api = some_api_lib.connect(some_api_token)
#              ...

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
