import scrapy


class KpiUspechyKatedrySpider(scrapy.Spider):
    name = 'kpi_uspechy_katedry'
    allowed_domains = ['kpi.fei.tuke.sk']
    start_urls = ['http://kpi.fei.tuke.sk/']

    def parse(self, response):
        pass
