import os

from CheckNewsProcess import CheckNewsProcess
from NewsCheckers import NewsChecker



#we need to run the scraper from here and
# all changing files will be here
os.chdir('aktuality_scrapers')


news_checkers_list = [NewsChecker("fei", "aktuality.csv", "API_KEY", "@fei_tuke_aktuality", True, True, True, False, True), NewsChecker("mais", "mais.csv", "API_KEY", "@fei_tuke_aktuality", True, False, True, False, False),
                       NewsChecker("tuke_oznamy", "tuke_oznamy.csv", "API_KEY", "@fei_tuke_aktuality", True, True, True, False, True), NewsChecker("tuke_aktuality", "tuke_aktuality.csv", "API_KEY", "@fei_tuke_aktuality", True, True, True, False, True),
                        NewsChecker('kpi_aktuality', 'kpi_aktuality.csv', 'API_KEY', '@fei_tuke_aktuality', True, True, True, False, True), NewsChecker('kpi_udalosti', 'kpi_udalosti.csv', 'API_KEY', '@fei_tuke_aktuality', True, True, True, False, True), NewsChecker('kpi_uspechy_katedry', 'kpi_uspechy_katedry.csv', 'API_KEY', '@fei_tuke_aktuality', True, True, True, False, True)]
process = CheckNewsProcess(news_checkers_list)
process.run()
