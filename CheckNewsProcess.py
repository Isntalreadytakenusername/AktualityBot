import os
import pandas as pd
import time


class CheckNewsProcess:
    def __init__(self, news_checkers_list):
        self.news_checkers_list = news_checkers_list

    def countdown_to_next_check(self):
        for i in range(60):
            print(f'Waiting {60-(i+1)} minutes before the next check')
            time.sleep(60)

    def run(self):
        while True:
            for news_checker in self.news_checkers_list:
                news_checker.check_for_new_posts()
                news_checker.check_whether_the_post_is_new()

            self.countdown_to_next_check()