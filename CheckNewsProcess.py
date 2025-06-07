import os
import pandas as pd
import time
from TelegramBot import TelegramBot

import traceback
import time
import sys


class CheckNewsProcess:
    def __init__(self, news_checkers_list):
        self.initial_dir = os.path.abspath(os.getcwd())
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

            except Exception as e:
                # Capture the full exception traceback
                error_message = traceback.format_exc()

                # Print the error message
                print('Something went wrong, restarting the script')
                print(error_message)

                # Send the full traceback to the logging_bot
                # self.logging_bot.send_logging_message(f'Something went wrong, restarting the script\n{error_message}')

                # Restart the script by re-executing the current program
                time.sleep(5)  # Optional: give it a short delay before restarting
                os.execv('/usr/bin/python3', ['/usr/bin/python3', '/home/ubuntu/AktualityBot/main.py'] + sys.argv[1:])
