import os
import pandas as pd
import time

from CheckNewsProcess import CheckNewsProcess
from NewsCheckers import NewsChecker
from TelegramBot import TelegramBot


##############################

#we need to run the scraper from here and
# all changing files will be here
os.chdir('aktuality_scrapers')


news_checkers_list = [NewsChecker("fei", "aktuality.csv", "API_KEY", "@fei_tuke_aktuality"), NewsChecker("mais", "mais.csv", "API_KEY", "@fei_tuke_aktuality", True, False, True, False, False)]
process = CheckNewsProcess(news_checkers_list)
process.run()
