import os
import telebot
import time
import requests

while 1:
  API_KEY = os.environ['API_KEY']
  
  bot = telebot.TeleBot(API_KEY)
  
  #bot.send_message(301011944696936, "Test message")
  requests.post('https://api.telegram.org/bot'+API_KEY+'/sendMessage?chat_id=-1001538579646&text=Hello World!')
  print("Message sent")
  time.sleep(5)
