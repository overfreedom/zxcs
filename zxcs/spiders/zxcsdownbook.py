# -*- coding: utf-8 -*-
import scrapy
import zxcs.database as db
from zxcs.items import ZxcsDownLoadItem

class ZxcsdownbookSpider(scrapy.Spider):
    name = 'zxcsdownbook'
    allowed_domains = ['www.zxcs.me']
    start_urls = []
    cs = db.connection.cursor()
    sql = 'select downloadurl from zxcsitem where xiancao - ducao > 100 '
    cs.execute(sql)
    result = cs.fetchall()
    for row in result:
        start_urls.append(row[0])

    def parse(self, response):
        item = ZxcsDownLoadItem()
        item['files'] = response.xpath('/html/body/div[2]/div[2]/h2/text()').get().strip()
        item['file_urls'] = [response.xpath('/html/body/div[2]/div[2]/div[3]/div[2]/span[1]/a/@href').get().strip()]

        return item

