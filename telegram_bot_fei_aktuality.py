import os
import telebot
import requests
import pandas




##################################FEI TUKE Aktuality##############################################
#read csv file to dataframe
aktuality_last_df = pandas.read_csv('aktuality_last.csv')

#prepare text to be posted

title = aktuality_last_df["title"][0]
date = aktuality_last_df["date"][0]
date = f"<code>{date}</code>"
image = aktuality_last_df["image"][0]
text = aktuality_last_df["text"][0]
link_to_aktuality_fei = "<a href = 'https://www.fei.tuke.sk/sk/studium/aktuality'><u><b>Aktuality FEI</b></u></a>"

if len(image) == 0:
  image = ""
else:
  image = f"<a href = '{image}'> <i> image </i> </a>"

text_to_post = f"<b>{title}</b>\n{date}\n{text}\n\n\n {link_to_aktuality_fei}\n{image}"

#prepare bot
API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

#send the message
bot.send_message(chat_id = '@fei_tuke_aktuality', text = text_to_post, parse_mode = 'HTML')
#requests.post(f'https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id=-1001538579646&text={text_to_post}')
print("Message sent")
