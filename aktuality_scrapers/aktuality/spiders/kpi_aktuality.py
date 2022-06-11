import scrapy


class KpiAktualitySpider(scrapy.Spider):
    name = 'kpi_aktuality'
    allowed_domains = ['kpi.fei.tuke.sk']
    start_urls = ['http://kpi.fei.tuke.sk/']

    def parse(self, response):
        pass
