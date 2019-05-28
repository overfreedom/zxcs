# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZxcsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    bookurl = scrapy.Field()
    author= scrapy.Field()
    size = scrapy.Field()
    sizeUnit= scrapy.Field()
    content = scrapy.Field()
    maintag= scrapy.Field()
    subtag = scrapy.Field()
    xiancao = scrapy.Field()
    liangcao = scrapy.Field()
    gancao= scrapy.Field()
    kucao = scrapy.Field()
    ducao = scrapy.Field()
    downloadurl = scrapy.Field()

    pass


class ZxcsDownLoadItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()