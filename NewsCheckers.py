import os
import pandas as pd
import time

from TelegramBot import TelegramBot


class NewsChecker:
    '''
    To use this object run check_for_new_posts and check_whether_the_post_is_new
    '''
    def __init__(self, scraper_name, scraper_output_file, environment_variable_with_api_key_for_bot, chat_id, is_text = True, is_title = True, is_date = True, is_image = True, is_link = True):
        self.scraper_name = scraper_name
        self.scraper_output_file = scraper_output_file
        self.last_scraper_output_file = self.scraper_output_file[:-4]+"_last.csv"
        
        self.scraper_output_df = None
        self.previous_output_df = None
        
        
        #create telegram bot
        self.telegram_bot = TelegramBot(self.last_scraper_output_file, environment_variable_with_api_key_for_bot, chat_id, is_text, is_title, is_date, is_image, is_link)
        self.telegram_bot.prepare_bot("API_KEY")

        # if there is no file History.csv, create it with columns text and date using pandas
        if not os.path.exists("History.csv"):
            df = pd.DataFrame(columns=["text", "date"])
            df.to_csv("History.csv", index=False)



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

                # now check whether the post was already recorded to History.csv. This is needed becouse new post may be deleted and the last post that was already published will be published
                # again. To avoid this, we check whether the post is already in History.csv
                history_df = pd.read_csv("History.csv")
                # check whether the post is already in History.csv using text and date fields. Check each row in History.csv and compare it to the last post (text and date)
                for i in range(len(history_df)):
                    if history_df["text"][i] == self.scraper_output_df["text"][0] and history_df["date"][i] == self.scraper_output_df["date"][0]:
                        print("The post was already sent")
                        return
                
                # if the post is not in History.csv, write it to History.csv and send it with the bot, use concat to add the new row to the dataframe
                history_df = pd.concat([history_df, self.scraper_output_df.iloc[0:1]])
                # delete History.csv and write the new dataframe to History.csv
                os.remove("History.csv")
                history_df.to_csv("History.csv", index=False)

                os.remove(self.last_scraper_output_file)
                self.scraper_output_df.to_csv(self.last_scraper_output_file, index=False)

                print(f"==============================THE MESSAGE IS SENT. UNCOMMENT LATER====================================\n")
                # self.telegram_bot.send_bots_message()
        else:
            self.scraper_output_df.to_csv(self.last_scraper_output_file, index=False)
            print(f"==============================THE MESSAGE IS SENT. UNCOMMENT LATER====================================")
            # self.telegram_bot.send_bots_message()