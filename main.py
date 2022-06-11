import os
import pandas as pd
import time

from CheckNewsProcess import CheckNewsProcess
from NewsCheckers import NewsChecker









##############################

#we need to run the scraper from here and
# all changing files will be here
os.chdir('aktuality_scrapers')


news_checkers_list = [NewsChecker("fei", "aktuality.csv", "telegram_bot_fei_aktuality.py"), NewsChecker("mais", "mais.csv", "telegram_bot_mais.py")]
process = CheckNewsProcess(news_checkers_list)
process.run()
