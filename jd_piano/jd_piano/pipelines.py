# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter


class JdPianoPipeline:
    def open_spider(self,item):
        self.fp = open(file=r'./pianos/pianos.json',mode='w',encoding='utf-8')
        # 因为生成的是json数组,所以需要给全部json字符串用[]括起来同时每分隔一个加一个',',同时还需要将单引号改为双引号
        self.fp.write('[')

    def process_item(self, item, spider):
        # 因为生成的是json数组,所以需要给全部json字符串用[]括起来同时每分隔一个加一个',',同时还需要将单引号改为双引号
        self.fp.write(str(item).replace('\'','"'))
        if item:
            self.fp.write(',')
        return item

    def close_spider(self,item):
        # 因为生成的是json数组,所以需要给全部json字符串用[]括起来同时每分隔一个加一个',',同时还需要将单引号改为双引号
        self.fp.write(']')
        self.fp.close()

