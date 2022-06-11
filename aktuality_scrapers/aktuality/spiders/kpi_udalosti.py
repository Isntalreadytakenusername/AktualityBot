import scrapy


class KpiUdalostiSpider(scrapy.Spider):
    name = 'kpi_udalosti'
    allowed_domains = ['kpi.fei.tuke.sk']
    start_urls = ['http://kpi.fei.tuke.sk/']

    def parse(self, response):
        pass
