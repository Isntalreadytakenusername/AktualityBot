import scrapy


class MaisSpider(scrapy.Spider):
    name = 'mais'
    allowed_domains = ['student.tuke.sk']
    start_urls = ['http://student.tuke.sk/']

    def parse(self, response):
        text = response.xpath("(//p[contains(@class, 'newsPriority')])[1]/a/text()").extract_first()
        date = response.xpath("(//p[contains(@class, 'newsPriority')])[1]/span[@class = 'xSmall']/text()").extract_first()
        text = text + '\n\n' + 'student.tuke.sk' + response.xpath("(//p[contains(@class, 'newsPriority')])[1]/a/@href").extract_first()
        yield {'text': text, 'date': date}
