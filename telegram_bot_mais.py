import os
import telebot
import requests
import pandas




################################## MAIS ##############################################
#read csv file to dataframe
aktuality_last_df = pandas.read_csv('mais_last.csv')

#prepare text to be posted

date = aktuality_last_df["date"][0]
date = f"<code>{date}</code>"
text = aktuality_last_df["text"][0]


text_to_post = f"{date}\n{text}"

#prepare bot
API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

#send the message
bot.send_message(chat_id = '@fei_tuke_aktuality', text = text_to_post, parse_mode = 'HTML')
#requests.post(f'https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id=-1001538579646&text={text_to_post}')
print("Message sent")
