import os
import telebot
import pandas as pd


class TelegramBot:
    '''
    Booleans may be determined by Spiders yields/output files, if respective field is available (ex. link), than it should be set true upon object's creation

    chat_id contains id of a channel (@username_of_channel) or a chat

    environment_variable_with_api_key_for_bot is a name of env variable with the token given upon bot's creation

    '''

    def __init__(self, last_scraper_output_file, environment_variable_with_api_key_for_bot, chat_id, is_text = True, is_title = True, is_date = True, is_image = True, is_link = True):
        self.last_scraper_output_file = last_scraper_output_file
        self.is_text = is_text
        self.is_date = is_date
        self.is_image = is_image
        self.is_link = is_link
        self.is_title = is_title
        self.environment_variable_with_api_key_for_bot = environment_variable_with_api_key_for_bot
        self.chat_id = chat_id

        self.bots_message = ""
        self.news_data_for_bot_df = None
        self.bot = None

    def prepare_bot(self, environment_variable_with_api_key_for_bot):
        API_KEY = os.environ[environment_variable_with_api_key_for_bot]
        bot = telebot.TeleBot(API_KEY)
        self.bot = bot

    def prepare_bots_message(self):
        self.news_data_for_bot_df = pd.read_csv(self.last_scraper_output_file)

        if self.is_title:
            self.bots_message += f"<b>{self.news_data_for_bot_df['title'][0]}</b>\n"
        if self.is_date:
            self.bots_message += f"<code>{self.news_data_for_bot_df['date'][0]}</code>\n"
        if self.is_text:
            self.bots_message += f"{self.news_data_for_bot_df['text'][0]}\n"
        if self.is_link:
            self.bots_message += f"\n\n{self.news_data_for_bot_df['link'][0]}\n"
        if self.is_image:
            self.bots_message += f"\n   <a href = '{self.news_data_for_bot_df['image'][0]}'> <i> image </i> </a>"

    def send_bots_message(self):
        self.prepare_bot(self.environment_variable_with_api_key_for_bot)
        self.prepare_bots_message()
        self.bot.send_message(chat_id = self.chat_id, text = self.bots_message, parse_mode = 'HTML')
        print("The message is sent")

        

        