import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class TukeAktualitySpider(scrapy.Spider):
    name = 'tuke_aktuality'
    allowed_domains = ['www.tuke.sk']
    start_urls = ['http://www.tuke.sk/']

    def parse(self, response):
      chrome_options = Options()
      chrome_options.add_argument('--headless')
      chrome_options.add_argument('--no-sandbox')
      chrome_options.add_argument('--disable-dev-shm-usage')
      driver = webdriver.Chrome(options=chrome_options)
      driver.set_window_size(1920, 1080)
      driver.get('https://www.tuke.sk/wps/portal/tuke/studies/st_news/!ut/p/z1/hc7BCsIwEATQb_ELdhO3SXpcqBaLjdFqrblIDlICGj2I328tvapzG3gDAx468Cm8Yh-e8Z7Cdegnr84qF1jOCevSaYNcLReZtkZiK-E4AvwSRvD_9n4kJIgFfYjeFcj59iAb0wqUYgJrzkhWA9gYJZHdam8Lqp3NcAI_PjSXBI9bh9H1szc7lCRI/dz/d5/L0lHSkovd0RNQUZrQUVnQSEhLzROVkUvc2s!/')
      time.sleep(5)
      #substitute response with driver.page_source
      response = scrapy.Selector(text=driver.page_source)

      date = response.xpath("(//time/text())[1]").extract_first()
      title = response.xpath("(//article//h1/a/text())[1]").extract_first()
      link = 'www.tuke.sk/wps/portal/tuke/university/news' + response.xpath("(//article//h1/a/@href)[1]").extract_first()
      text = response.xpath("(//article//p/text())[1]").extract_first()
      # all = response.xpath("//html//text()").extract()
      # yield {'all': all}
      yield {'date': date.strip(), 'title': title.strip(), 'link': link.strip(), 'text': text.strip()}
