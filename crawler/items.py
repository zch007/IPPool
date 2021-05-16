"""定义scrapy数据管道接收的数据字段"""

import scrapy


class IPItem(scrapy.Item):
    host = scrapy.Field()
    port = scrapy.Field()
    proxy_type = scrapy.Field()
    anonymity_type = scrapy.Field()
    region = scrapy.Field()

