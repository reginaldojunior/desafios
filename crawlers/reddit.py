import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class RedditSpider(scrapy.Spider):
    name = 'redditspider'
    subreddit = 'r/brasil'
    start_urls = ['https://www.reddit.com/' + subreddit +'/top/?sort=top&t=year']

    def parse(self, response):
		selected = Selector(response)	
		reddits = selected.css('div.link')
		
		for reddit in reddits:
			upvotes = reddit.css('div.likes::text').extract_first()

			if int(upvotes) >= 5000:
				yield {
					'upvotes': upvotes,
					'title': reddit.css('p.title a::text').extract_first(),
					'link': reddit.css('p.title a::attr(href)').extract_first(),
					'subreddit': self.subreddit,
					'comments': reddit.css('li.first a::attr(href)').extract_first()
				}

		for next_page in response.css('span.next-button > a'):
			yield response.follow(next_page, self.parse)