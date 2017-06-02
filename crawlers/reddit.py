import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class RedditSpider(scrapy.Spider):
    name = 'redditspider'
    start_urls = ['https://www.reddit.com/r/brasil/']

    def parse(self, response):
		selected = Selector(response)	
		reddits = selected.css('div.link')
		
		for reddit in reddits:
			print "https:" + str(reddit.css('a.thumbnail img::attr(src)').extract_first())
			print reddit.css('div.likes::text').extract_first()

        # for next_page in response.css('div.prev-post > a'):
        #     yield response.follow(next_page, self.parse)