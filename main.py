import os

from CheckNewsProcess import CheckNewsProcess
from NewsCheckers import NewsChecker

# for replit not to give nasty permission errors regarding scrapy 
os.system("chmod +rwx venv/bin/scrapy")


#we need to run the scraper from here and
# all changing files will be here
os.chdir('aktuality_scrapers')

telegram_channel_id = '@fei_tuke_aktuality'
# telegram_channel_id = '@aktuality_testing'

# # Temporarily removed tuke_oznamy as there is a mysterious problem with tuke oznamy and I have an exam period
# news_checkers_list = [NewsChecker("fei", "aktuality.csv", "API_KEY", telegram_channel_id, True, True, True, False, True), NewsChecker("mais", "mais.csv", "API_KEY", telegram_channel_id, True, False, True, False, False),
#                        NewsChecker("tuke_aktuality", "tuke_aktuality.csv", "API_KEY", telegram_channel_id, True, True, True, False, True),
#                         NewsChecker('kpi_aktuality', 'kpi_aktuality.csv', 'API_KEY', telegram_channel_id, True, True, True, False, True), NewsChecker('kpi_udalosti', 'kpi_udalosti.csv', 'API_KEY', telegram_channel_id, True, True, True, False, True), NewsChecker('kpi_uspechy_katedry', 'kpi_uspechy_katedry.csv', 'API_KEY', telegram_channel_id, True, True, True, False, True)]

# The old version with tuke_oznamy
news_checkers_list = [NewsChecker("fei", "aktuality.csv", "API_KEY", telegram_channel_id, True, True, True, False, True), NewsChecker("mais", "mais.csv", "API_KEY", telegram_channel_id, True, False, True, False, False),
                       NewsChecker("tuke_oznamy", "tuke_oznamy.csv", "API_KEY", "@aktuality_testing", True, True, True, False, True), NewsChecker("tuke_aktuality", "tuke_aktuality.csv", "API_KEY", telegram_channel_id, True, True, True, False, True),
                        NewsChecker('kpi_aktuality', 'kpi_aktuality.csv', 'API_KEY', telegram_channel_id, True, True, True, False, True), NewsChecker('kpi_udalosti', 'kpi_udalosti.csv', 'API_KEY', telegram_channel_id, True, True, True, False, True), NewsChecker('kpi_uspechy_katedry', 'kpi_uspechy_katedry.csv', 'API_KEY', telegram_channel_id, True, True, True, False, True)]
process = CheckNewsProcess(news_checkers_list)
process.run()




