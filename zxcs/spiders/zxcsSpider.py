# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ZxcsItem
import re
import requests
import random

class ZxcsspiderSpider(CrawlSpider):
    name = 'zxcsSpider'
    allowed_domains = ['www.zxcs.me']
    start_urls = ['http://www.zxcs.me/map.html']

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
    }

    cmpl = re.compile(r'/(\d+)$')

    rules = (
        Rule(LinkExtractor(allow=r'http://www.zxcs.me/post/\d+'),
             callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'http://www.zxcs.me/sort/\d+/page/\d+'), follow=True),
        Rule(LinkExtractor(allow=r'http://www.zxcs.me/sort/\d+'), follow=True),
    )

    def get_mood(self, url):
        try:
            response = requests.get(url,headers = self.headers)
            if 300 > response.status_code >= 200 :
                return response.text                
        except requests.ConnectionError as e:   
             print('error', e.args)

    def parse_item(self, response):
        item = ZxcsItem()
        item['bookurl'] = response.url.strip()
        id = re.search(self.cmpl, item['bookurl']).group(1)
        tmpurl = 'http://www.zxcs.me/content/plugins/cgz_xinqing/cgz_xinqing_action.php?action=show&id='+id+'&m='+str(random.random())
        moodstr = self.get_mood(tmpurl)        
        moodls = moodstr.split(',')
        tmptitle = response.xpath('//div[@id="content"]/h1/text()').get()
        tmptitle = tmptitle.split('作者')
        item['title'] = tmptitle[0].strip()
        item['author'] = tmptitle[1].strip()
        tmpstr = response.xpath(
            '//div[@id="content"]/p[re:test(text(),"【TXT大小】")]/text()').get()
        reg = re.compile(r'(\d+\.?\d+)[\b]*([\w\W]+)')
        ls = reg.findall(tmpstr)

        if ls:
            item['size'] = ls[0][0].strip()
            item['sizeUnit'] = ls[0][1].strip()
        item['content'] = response.xpath(
            '//*[@id="content"]/p[3]/text()').get().strip()
        item['maintag'] = response.xpath(
            '//*[@id="content"]/p[1]/a[2]/text()').get().strip()
        item['subtag'] = response.xpath(
            '//*[@id="content"]/p[1]/a[3]/text()').get().strip()
        if len(moodls) == 5:
            item['xiancao'] = moodls[0]
            item['liangcao'] = moodls[1]
            item['gancao'] = moodls[2]
            item['kucao'] = moodls[3]
            item['ducao'] = moodls[4]
        item['downloadurl'] = response.xpath(
            '//*[@id="content"]/div[2]/div[3]/a/@href').get().strip()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()

        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
