import scrapy


class FeiSpider(scrapy.Spider):
    name = 'fei'
    allowed_domains = ['www.fei.tuke.sk']
    start_urls = ['https://www.fei.tuke.sk/sk/archive/clanky?category=aktuality_studijne_oddelenie']

    def parse(self, response):
        # Base XPath for the latest article (second one to skip language switch)
        base_xpath = "(//div[@role='button'][contains(@class, 'flex')][contains(@class, 'cursor-pointer')])[2]"
        
        # concatenated XPaths for developer tools checks:
        # For title: (//div[@role='button'][contains(@class, 'flex')][contains(@class, 'cursor-pointer')])[2]//h3/text()
        # For date: (//div[@role='button'][contains(@class, 'flex')][contains(@class, 'cursor-pointer')])[2]//p[contains(@class, 'text-customGray-500')]/text()
        # For image: (//div[@role='button'][contains(@class, 'flex')][contains(@class, 'cursor-pointer')])[2]//img/@src
        # For link: (//div[@role='button'][contains(@class, 'flex')][contains(@class, 'cursor-pointer')])[2]//a/@href
        
        latest_article = response.xpath(base_xpath)
        
        if latest_article:
            # Extract title from h3
            post_title = latest_article.xpath(".//h3/text()").get('').strip()
            
            # Extract date from p with class text-customGray-500
            date_of_post = latest_article.xpath(".//p[contains(@class, 'text-customGray-500')]/text()").get('').strip()
            
            # Extract image URL from img tag
            image_url = latest_article.xpath(".//img/@src").get('')
            
            # Extract link to the full article
            article_link = latest_article.xpath(".//a/@href").get('')
            full_link = f"https://www.fei.tuke.sk{article_link}" if article_link else "https://www.fei.tuke.sk/sk/archive/clanky?category=aktuality_studijne_oddelenie"
            
            # Since there's no direct text in this preview, we'll need to follow the link to get the full text
            # it can be followed in a callback, but it is not necessary for the purpose of this spider
            text_of_post = ""
            
            yield {
                'title': post_title,
                'date': date_of_post,
                'image': image_url,
                'text': text_of_post,
                'link': full_link
            }
        else:
            self.log("No articles found on the page")