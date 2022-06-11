import os
import pandas as pd
import time


class NewsChecker:
    '''
    To use this object run check_for_new_posts and check_whether_the_post_is_new
    '''
    def __init__(self, scraper_name, scraper_output_file, bot_script_name):
        self.scraper_name = scraper_name
        self.scraper_output_file = scraper_output_file
        self.last_scraper_output_file = self.scraper_output_file[:-4]+"_last.csv"
        self.bot_script_name = bot_script_name
        
        self.scraper_output_df = None
        self.previous_output_df = None

    def check_for_new_posts(self):
        # check if the file already exists, delete
        if os.path.exists(self.scraper_output_file):
            os.remove(self.scraper_output_file)

        #get the data with scraper
        print("Checking for new posts...")
        os.system(f"scrapy crawl {self.scraper_name} -o {self.scraper_output_file}")
        self.scraper_output_df = pd.read_csv(self.scraper_output_file)
        print("The last posts are acquired")

    def is_previous_output(self):
        return os.path.exists(self.last_scraper_output_file)

    def save_previous_output_to_dataframe(self):
        if self.is_previous_output():
            self.previous_output_df = pd.read_csv(self.last_scraper_output_file)
            return True
        else:
            return False

    def check_whether_the_post_is_new(self):
        #if we have results from previous check, compare to them, if no, we consider the last information to be new
        #and send it with the bot
        if self.save_previous_output_to_dataframe():
            if self.scraper_output_df["text"][0] == self.previous_output_df["text"][0]:
                print("No new posts")
            else:
                print("New post found")
                os.remove(self.last_scraper_output_file)
                self.scraper_output_df.to_csv(self.last_scraper_output_file, index=False)
                os.system(f"python ../{self.bot_script_name}")
        else:
            self.scraper_output_df.to_csv(self.last_scraper_output_file, index=False)
            os.system(f"python ../{self.bot_script_name}")
        # check whether we have last results