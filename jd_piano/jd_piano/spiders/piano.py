import json

import scrapy
from jd_piano.items import JdPianoItem

class PianoSpider(scrapy.Spider):
    name = 'piano'
    allowed_domains = ['jd.com']
    start_urls = ['https://list.jd.com/list.html?cat=6233%2C18615%2C18686&psort=4&psort=4&page=1&s=1&click=0']
    page = 1

    def parse(self, response):
        # 将18页的数据封装成json格式存储
        # 将18页的数据封装成json格式存储
        pj = json.load(open(file=r'./pages/pages.json', mode='r', encoding='utf-8'))

        # 这里通过xpath获取到每一页每一个商品的li,这里的返回值是list
        li_list = response.xpath('//ul[@class="gl-warp clearfix"]//li')

        for i in range(len(li_list)):
            brand_ = li_list[i].xpath('.//div[@class="gl-i-wrap"]//div[@class="p-name p-name-type-3"]//i/text()').extract_first()
            brand = str(brand_).split(' ')[0]
            if brand:
                brand = brand
            else:
                brand = 'None'
            piano = JdPianoItem(brand=brand)
            yield piano

        if self.page < 18:
            url = pj[self.page][str(self.page+1)]
            self.page = self.page + 1
            yield scrapy.Request(url=url,callback=self.parse)





