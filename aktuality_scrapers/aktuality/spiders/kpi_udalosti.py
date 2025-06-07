import scrapy


class KpiUdalostiSpider(scrapy.Spider):
    name = 'kpi_udalosti'
    allowed_domains = ['kpi.fei.tuke.sk']
    start_urls = ['https://kpi.fei.tuke.sk/sk/udalosti']

    def parse(self, response):
        title = response.xpath("(//span[@class = 'field-content'])[1]/a/text()").extract_first()
        link = "https://kpi.fei.tuke.sk" + response.xpath("(//span[@class = 'field-content'])[1]/a/@href").extract_first()
        text = response.xpath("(//div[@class = 'views-field views-field-body'])[1]/span/text()").extract_first()
        date = response.xpath("(//span[@class = 'field-content news-date'])[1]/text()").extract_first()
        image = response.xpath("(//img[contains(@src, 'header')])[1]/@src").extract_first()
        yield {'title': title, 'link': link, 'text': text, 'date': date, 'image': image}
