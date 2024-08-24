import os
import pandas as pd
import time
from TelegramBot import TelegramBot


class CheckNewsProcess:
    def __init__(self, news_checkers_list):
        self.news_checkers_list = news_checkers_list
        self.logging_bot = TelegramBot(None, "API_KEY", '@aktuality_testing', False, False, False, False, False)

    def countdown_to_next_check(self):
        for i in range(60):
            print(f'Waiting {60-(i+1)} minutes before the next check')
            self.logging_bot.send_logging_message(f'Waiting {60-(i+1)} minutes before the next check')
            time.sleep(60)

    def run(self):
        while True:
            try:
                for news_checker in self.news_checkers_list:
                    news_checker.check_for_new_posts()
                    news_checker.check_whether_the_post_is_new()

                self.countdown_to_next_check()
            except:
                print('Something went wrong, trying again in 5 minutes')
                self.logging_bot.send_logging_message('Something went wrong, trying again in 5 minutes')
                time.sleep(300)
                continue