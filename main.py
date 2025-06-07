import os

from CheckNewsProcess import CheckNewsProcess
from NewsCheckers import NewsChecker

# # for replit not to give nasty permission errors regarding scrapy 
# os.system("chmod +rwx venv/bin/scrapy")

# Path configuration for different environments
ubuntu_path = '/home/ubuntu/AktualityBot/aktuality_scrapers'
mac_path = '/Users/vlad/Documents/GitHub/AktualityBot/aktuality_scrapers'

# Determine the appropriate path based on the environment
if os.path.exists(ubuntu_path):
    scrapers_path = ubuntu_path
    print(f"Running on Ubuntu server: {ubuntu_path}")
elif os.path.exists(mac_path):
    scrapers_path = mac_path
    print(f"Running on Mac: {mac_path}")
else:
    raise FileNotFoundError(f"Neither {ubuntu_path} nor {mac_path} exists. Please check your installation paths.")

# Change to the scrapers directory
os.chdir(scrapers_path)

telegram_channel_id = '@fei_tuke_aktuality'
# telegram_channel_id = '@aktuality_testing'
telegram_channel_id = '@testing_shitsink'

# Temporarily removed the ones using tuke.sk
news_checkers_list = [NewsChecker("tuke_aktuality", "tuke_aktuality.csv", "API_KEY", telegram_channel_id, True, True, True, False, True), NewsChecker("fei", "aktuality.csv", "API_KEY", telegram_channel_id, True, True, True, False, True), NewsChecker("mais", "mais.csv", "API_KEY", telegram_channel_id, True, False, True, False, False),
                        NewsChecker('kpi_aktuality', 'kpi_aktuality.csv', 'API_KEY', telegram_channel_id, True, True, True, False, True), NewsChecker('kpi_udalosti', 'kpi_udalosti.csv', 'API_KEY', telegram_channel_id, True, True, True, False, True), NewsChecker('kpi_uspechy_katedry', 'kpi_uspechy_katedry.csv', 'API_KEY', telegram_channel_id, True, True, True, False, True)]

process = CheckNewsProcess(news_checkers_list)
process.run()




