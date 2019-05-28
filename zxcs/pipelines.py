# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import hashlib
import zxcs.database as db
from zxcs.items import ZxcsItem


cursor = db.connection.cursor()

class ZxcsPipeline(object):
    def save_bookinfo(self, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        tmp = ','.join(['%s']* len(keys))
        sql = 'insert into zxcsitem (%s) values (%s)' % (fields, tmp) 
        cursor.execute(sql, values)
        return db.connection.commit()

    def process_item(self, item, spider):
        try:
            self.save_bookinfo(item)
        except Exception as e:
            print(item)
            print(e)
        return item    
