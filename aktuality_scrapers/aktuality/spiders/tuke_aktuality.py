import scrapy
import dateutil.parser
from datetime import datetime

class TukeAktualitySpider(scrapy.Spider):
    name = 'tuke_aktuality'
    allowed_domains = ['tuke.sk', 'api.prod.tuke.sk']
    
    # Define the feed URLs
    feed_urls = [
        'https://api.prod.tuke.sk/feed/1/sk/articles-feed_university-highlights',
        'https://api.prod.tuke.sk/feed/1/sk/articles-feed_novinky',
        'https://api.prod.tuke.sk/feed/1/sk/articles-feed_udalosti',
        'https://api.prod.tuke.sk/feed/1/sk/articles-feed_media',
        'https://api.prod.tuke.sk/feed/1/sk/articles-feed_verejne-obstaravanie',
        'https://api.prod.tuke.sk/feed/1/sk/articles-feed_ulysseus',
        'https://api.prod.tuke.sk/feed/1/sk/articles-feed_veda-a-vyskum',
        'https://api.prod.tuke.sk/feed/1/sk/articles-feed_nezaradene'
    ]
    
    def __init__(self, *args, **kwargs):
        super(TukeAktualitySpider, self).__init__(*args, **kwargs)
        # Dictionary to store the latest article from each feed
        self.latest_articles = {}
        # Counter to track processed feeds
        self.feeds_processed = 0
    
    def start_requests(self):
        """Generate requests for each feed URL"""
        for url in self.feed_urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'feed_url': url})

    def _fix_tuke_url(self, url):
        """Fix incorrect URL format by removing the '/1' segment"""
        if url and 'tuke.sk/1/' in url:
            return url.replace('tuke.sk/1/', 'tuke.sk/')
        return url

    def parse(self, response):
        """Parse the XML feed and find the most recent article"""
        feed_url = response.meta['feed_url']
        
        # Extract all items from the feed
        items = response.xpath('//item')
        
        if not items:
            self.logger.info(f"Feed {feed_url} is empty or contains no items")
        
        if items:
            # Find the most recent article in this feed
            latest_date = None
            latest_article = None
            
            for item in items:
                title = item.xpath('title/text()').get()
                link = item.xpath('link/text()').get()
                # Fix the URL format
                link = self._fix_tuke_url(link)
                
                text = item.xpath('description/text()').get()
                date_str = item.xpath('pubDate/text()').get()
                
                if title and link and date_str:
                    try:
                        # Parse the date string
                        parsed_date = dateutil.parser.parse(date_str)
                        
                        # Check if this is the most recent article
                        if latest_date is None or parsed_date > latest_date:
                            latest_date = parsed_date
                            latest_article = {
                                'date': parsed_date,
                                'formatted_date': parsed_date.strftime('%d.%m.%Y'),
                                'title': title.strip(),
                                'link': link.strip(),
                                'text': text.strip() if text else '',
                                'feed_url': feed_url
                            }
                    except Exception as e:
                        self.logger.error(f"Error parsing date: {e}")
            
            # Store the most recent article from this feed
            if latest_article:
                self.latest_articles[feed_url] = latest_article
        
        # Increment the counter of processed feeds
        self.feeds_processed += 1
        
        # If all feeds have been processed, yield the most recent article overall
        if self.feeds_processed >= len(self.feed_urls):
            most_recent_article = self._get_most_recent_article()
            if most_recent_article:
                yield {
                    'date': most_recent_article['formatted_date'],
                    'title': most_recent_article['title'],
                    'link': most_recent_article['link'],
                    'text': most_recent_article['text']
                }
    
    def _get_most_recent_article(self):
        """Find the most recent article from all feeds"""
        most_recent = None
        most_recent_date = None
        
        for feed_url, article in self.latest_articles.items():
            if most_recent_date is None or article['date'] > most_recent_date:
                most_recent_date = article['date']
                most_recent = article
        
        return most_recent
