import scrapy
# import os
#
from xiaohua.items import XiaohuaItem
#
class XhSpider(scrapy.Spider):
    name='xh'
    allowed_domains=['xiaohua100.cn']
    start_urls=[
        'http://www.xiaohua100.cn/daxue/'
    ]
#
    def parse(self, response):
        # 获取所有图片标签
        print(response.url)
        print('-----------------------------------------------------------------------------------------------------------------------')
        allpics=response.xpath('//div[@class="pic"]/a')
        # print(allpics)
        for pic in allpics:
            # 分别处理每个图片，取出名称和地址
            item=XiaohuaItem()
            name=pic.xpath('./img/@alt').extract()[0]
            addr=pic.xpath('./img/@src').extract()[0]
            addr='http://www.xiaohua100.cn'+addr
            item['name']=name
            item['addr']=addr
            # print(item)
            yield item
# 进阶篇 获取图片
print('-----------------------------------------------------------------------------------------------------------------------')

# import scrapy
# import os
# from scrapy.http import Request
# from xiaohua.items import XiaohuaItem
#
# class XhSpider(scrapy.Spider):
#     name='xh'
#     allowed_domains=['xiaohua100.cn']
#     start_urls=[
#         'http://www.xiaohua100.cn/index.html'
#     ]
#     url_set=set()
#     def parse(self, response):
#         # 获取所有图片标签
#         if response.url.startswith("http://www.xiaohua100.cn/daxue/")
#             allpics=response.xpath('//div[@class="pic"]/a')
#         # print(allpics)
#             for pic in allpics:
#                 # 分别处理每个图片，取出名称和地址
#                 item=XiaohuaItem()
#                 name=pic.xpath('./img/@alt').extract()[0]
#                 addr=pic.xpath('./img/@src').extract()[0]
#                 addr='http://www.xiaohua100.cn'+addr
#                 item['name']=name
#                 item['addr']=addr
#                 # print(item)
#                 yield item
#         urls=response.xpath('//a/@href').extrct()
#         for url in urls:
#             if url.startswith("http://www.xiaohua100.cn/"):
#                 if url in XhSpider.url_set
#                     pass
#                 else:
#                     XhSpider.url_set.add(url)
#                     yield self.make_requests_from_url(url)
#             else:
#                 pass
