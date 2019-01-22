# -*- coding: utf-8 -*-
import scrapy
from Crawler.items import CrawlerItem



class WuxiareviewSpider(scrapy.Spider):
    name = 'wuxiareview'
    allowed_domains = ['www.wuxiareview.com']
    start_urls = ['https://www.wuxiareview.com/category/gzmdzst/',
                  'https://www.wuxiareview.com/category/xuanchu/',
                  'https://www.wuxiareview.com/category/xccsl/',
                  'https://www.wuxiareview.com/category/daidai/',
                  'https://www.wuxiareview.com/category/sand/',
                  'https://www.wuxiareview.com/category/news/',]


    def parse(self, response):
        articles = response.css('body > section > div > div > article')
        for article in articles:
            url = article.css('.focus::attr(href)').extract_first()
            yield scrapy.Request(url,callback=self.info_parse)

        # 翻页
        next = response.css('.next-page > a::attr(href)').extract_first()
        next_url = response.urljoin(next)
        if next_url:
            yield scrapy.Request(url=next_url,callback=self.parse)
        else:
            return None

    def info_parse(self,reponse):
        item = CrawlerItem()
        article = reponse.css('.content')
        item['datetime'] = article.css('.article-meta .item::text').extract_first()
        item['category'] = article.css('.article-meta .item > a::text').extract_first()
        item['title'] = article.css('.article-title > a::text').extract_first()
        item['info'] = article.css('.article-content > p::text').extract()

        yield item