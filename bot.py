# -*- coding: utf-8 -*-
import redis
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEG_TOKEN']
#api_token = os.environ['API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
# bot = telebot.TeleBot(594779131:AAGStMS5a9vcfmjjKdI9HSaxjHq4SsKhRnw)
# some_api = some_api_lib.connect(some_api_token)
#              ...
