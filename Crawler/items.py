# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标签
    category = scrapy.Field()
    # 时间
    datetime = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 正文
    info = scrapy.Field()
    # 摘要
    note = scrapy.Field()
    # url网址
    url = scrapy.Field()

