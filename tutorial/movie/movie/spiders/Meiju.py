import scrapy

from movie.items import MovieItem

class MeijuSpider(scrapy.Spider):
    name='meijuscra'
    allowed_domains=['meijutt.com']
    start_urls=[
        # 'http://www.mm131.com/qingchun/',
        # 'http://www.meijutt.com/content/meiju23226.html'
        'http://www.meijutt.com/new100.html'
        # 'http://www.meijutt.com'
    ]
    def parse(self,response):
        # movies=response.url.split('/')[-2]
        # filename=response.url.split('/')[-2]
        # with open(filename,'wb') as f:
        #     f.write(response.body)
        # sel=scrapy.selector.Selector(response)
        sites=response.xpath('//ul[@class="top-list  fn-clear"]/li')
        # items=[]
        for site in sites:
            # title=site.xpath('a/text()').extract()
            # link=
            # print(title)
            item=MovieItem()
            item['filmname']=site.xpath('./h5/a/@title').extract()[0]
            # items.append(item)
            # print(item)
            yield item