import scrapy


class FeiSpider(scrapy.Spider):
    name = 'fei'
    allowed_domains = ['www.fei.tuke.sk']
    start_urls = ['https://www.fei.tuke.sk/sk/studium/aktuality/']

    def parse(self, response):
        last_post = response.xpath("(//div[contains(@id, 'article')])[1]")
        post_title = last_post.xpath("((//div[contains(@id, 'article')])[1]//div[@class = 'nazov_stranky']//text())[2]").extract_first()
        date_of_post = last_post.xpath("((//div[contains(@id, 'article')])[1]//div[contains(@class , 'articleContent')]/div[@class = 'description']/p/text())[1]").extract_first()
        link_to_post_image = last_post.xpath("((//div[contains(@id, 'article')])[1]//div[contains(@class , 'articleContent')]/div[@class = 'description']/p/img/@src)[1]").extract_first()
        text_of_post = last_post.xpath("((//div[contains(@id, 'article')])[1]//div[contains(@class , 'articleContent')]/div[@class = 'description']/p[contains(@style, 'text-align')]//text())").extract()
        # join all strings in text_of_post list 
        text_of_post = ' '.join(text_of_post)
        yield {'title': post_title, 'date': date_of_post, 'image': link_to_post_image, 'text': text_of_post, 'link': 'https://www.fei.tuke.sk/sk/studium/aktuality'}


