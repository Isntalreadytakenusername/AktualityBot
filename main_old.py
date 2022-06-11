import os
import pandas
import time

#we need to run the scraper from here and
# all changing files will be here
os.chdir('aktuality_scrapers')

while True:
    print("Checking for new posts...")
    #check if the file exists delete
    if os.path.exists('aktuality.csv'):
        os.remove('aktuality.csv')
        # read the file as pandas dataframe

    os.system('scrapy crawl fei -o aktuality.csv')
    aktuality_df = pandas.read_csv('aktuality.csv')
    print("The last post is acquired")

    if os.path.exists('aktuality_last.csv'):
        aktuality_last_df = pandas.read_csv('aktuality_last.csv')
        if aktuality_df["text"][0] == aktuality_last_df["text"][0]:
            print("No new posts")
        else:
            print("New post found")
            os.remove('aktuality_last.csv')
            aktuality_df.to_csv('aktuality_last.csv', index=False)
            os.system("python ../telegram_bot_fei_aktuality.py")
    else:
        aktuality_df.to_csv('aktuality_last.csv', index=False)
        os.system("python ../telegram_bot_fei_aktuality.py")

    #countdown to next check
    for i in range(60):
      print(f'Waiting {60-(i+1)} minutes before the next check')
      time.sleep(60)
