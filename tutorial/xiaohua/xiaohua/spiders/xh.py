import scrapy
import re
import json
from scrapy import Request
#
from xiaohua.items import XiaohuaItem
#
class XhSpider(scrapy.Spider):
    name='xhua'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    # allowed_domains=['xiaohua100.cn']
    # start_urls=[
    #     "http://www.xiaohua100.cn/plus/waterfall.php?tid=0&sort=lastpost&totalresult=890&pageno=2&r=0"
    #     ".8747465558656402&display=pic&isAjax=1&l=1358747256127773&ts=135874808804&tk=cb50cab524b3be07ac28fc6141350f86 "
       # 'http://www.xiaohua100.cn/index.html'
       #  ]
    def start_requests(self):
        url='http://www.xiaohua100.cn/plus/waterfall.php?tid=0&sort=lastpost&totalresult=890&pageno=1&r=0.8628859472707042&display=pic&isAjax=1&l=1358747256127773&ts=135874808804&tk=cb50cab524b3be07ac28fc6141350f86'
        yield Request(url,headers=self.headers)
    def parse(self, response):
        # 获取所有图片标签
        # print(response.url)
        print('-----------------------------------------------------------------------------------------------------------------------')
        # datas=json.loads(response.body)
        # allpics=response.xpath('//div[@class="pic"]/a')
        allin=response.xpath('//div')

        # print(allpics)
        # for pic in allpics:
        for pic in allin:
            # 分别处理每个图片，取出名称和地址
            item=XiaohuaItem()
            if pic.xpath('./h3/span[@class="cellTit"]/a/text()').extract():
                name = pic.xpath('./h3/span[@class="cellTit"]/a/text()').extract()
            # name=pic.xpath('./img/@src').extract()[0]
            # name=name.split('/')[-1]
            if pic.xpath('./div[@class="pic"]/a/img/@src').extract():
                addr=pic.xpath('./div[@class="pic"]/a/img/@src').extract()[0]
            # addr=pic.xpath('./img/@src').extract()[0]
            addr='http://www.xiaohua100.cn'+addr
            item['name']=name
            item['addr']=addr
            # print(item)
            yield item

        page_add=re.search(r'pageno=(\d+)',response.url).group(1)
        page_add='pageno='+ str(int(page_add)+1)
        next_url=re.sub(r'pageno=\d+',page_add,response.url)
        yield Request(next_url,headers=self.headers)
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
