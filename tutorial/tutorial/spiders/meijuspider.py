# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

from tutorial.items import MovieItem

class MeijuSpider(scrapy.Spider):
    name='meiju'
    allowed_domains=['meijutt.com']
    start_urls=[
        # 'http://www.mm131.com/qingchun/',
        # 'http://www.meijutt.com/content/meiju23226.html'
        'http://www.meijutt.com'
    ]
    def parse(self,response):
        # movies=response.url.split('/')[-2]
        # filename=response.url.split('/')[-2]
        # with open(filename,'wb') as f:
        #     f.write(response.body)
        sel=scrapy.selector.Selector(response)
        sites=sel.xpath('//ul[@class="navUl"]/li')
        items=[]
        for site in sites:
            # title=site.xpath('a/text()').extract()
            # link=
            # print(title)
            item=MovieItem()
            item['title']=site.xpath('a/text()').extract()
            items.append(item)
        return items

