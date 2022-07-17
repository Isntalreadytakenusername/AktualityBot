import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class TukeOznamySpider(scrapy.Spider):
    name = 'tuke_oznamy'
    allowed_domains = ['www.tuke.sk']
    start_urls = ['https://www.tuke.sk/wps/portal/tuke/university/news']

    def parse(self, response):
      chrome_options = Options()
      chrome_options.add_argument('--headless')
      chrome_options.add_argument('--no-sandbox')
      chrome_options.add_argument('--disable-dev-shm-usage')
      driver = webdriver.Chrome(options=chrome_options)
      driver.set_window_size(1920, 1080)
      driver.get('https://www.tuke.sk/wps/portal/tuke/university/news/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zifRxNTYy8TAx83Z093AwcA0IDA00dnQz83Y30w8EKDHAARwP9KEL6o8BKTAxNHA1NQErMg1wMHC0DQ42CLcIMDSyMoQrgZvhbmBkBzfAM8XMx8Q3wMzWAKsDjhuDUPP2C3AiDzIB0RQALdY9q/dz/d5/L0lHSkovd0RNQUZrQUVnQSEhLzROVkUvc2s!/')
      time.sleep(5)
      #substitute response with driver.page_source
      response = scrapy.Selector(text=driver.page_source)

      date = response.xpath("(//time/text())[1]").extract_first()
      title = response.xpath("(//article//h1/a/text())[1]").extract_first()
      link = 'www.tuke.sk' + response.xpath("(//article//h1/a/@href)[1]").extract_first()
      text = response.xpath("(//article//p/text())[1]").extract_first()
      # all = response.xpath("//html//text()").extract()
      # yield {'all': all}
      yield {'date': date.strip(), 'title': title.strip(), 'link': link.strip(), 'text': text.strip()}
