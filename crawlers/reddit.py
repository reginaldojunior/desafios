# -*- coding: utf-8 -*-

import scrapy
import requests
import urllib
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class RedditSpider(scrapy.Spider):
    name = 'redditspider'
    subreddit = ''
    chat_id = ''
    endpoint = 'https://api.telegram.org/bot390538628:AAFEBJzvhs2OZky4UCPUt4vLH21RbVjU2dg/sendMessage'

    def __init__(self, subreddit='r/brasil', chat_id='', *args, **kwargs):
        super(RedditSpider, self).__init__(*args, **kwargs)

        self.subreddit = subreddit
        self.chat_id = chat_id
        self.start_urls = ['https://www.reddit.com/' +
                           subreddit + '/top/?sort=top&t=year']

    def parse(self, response):
        selected = Selector(response)
        reddits = selected.css('div.link')

        for reddit in reddits:
            upvotes = False

            try:
                upvotes = int(reddit.css('div.likes::text').extract_first())
            except Exception, e:
                upvotes = True

            if upvotes >= 5000 or upvotes is True:
                text = '*Up Votes*: ' + \
                    reddit.css('div.likes::text').extract_first() + '\n'
                text += '*Titulo*: ' + \
                    reddit.css('p.title a::text').extract_first() + '\n'
                text += '*Link*: [Acesse o Reddit](https://www.reddit.com/' + reddit.css(
                    'p.title a::attr(href)').extract_first() + ')\n'
                text += '*SubReddit*: [Veja todos Reddits](https://www.reddit.com/' + \
                    self.subreddit + ')\n'
                text += '*Comments*: [Comentarios do Reddit](' + reddit.css(
                    'li.first a::attr(href)').extract_first() + ')'

                yield requests.get(self.endpoint + '?chat_id=' + self.chat_id + '&text=' + text + '&parse_mode=Markdown')
