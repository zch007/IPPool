import scrapy
from bs4 import BeautifulSoup

from crawler.items import IPItem
from utils.cache import Cache
from utils.field_parse import FieldParser


class SixSixIpSpider(scrapy.Spider):
    name = "66ip"
    page = 1

    def start_requests(self):
        while True:

            if self.page == 2400:
                break

            url = "http://www.66ip.cn/{}.html".format(self.page)
            self.page += 1
            yield scrapy.Request(url)

    def parse(self, response, **kwargs):
        res = response.body

        soup = BeautifulSoup(res, "lxml")
        table = soup.find_all("table")[2]
        tr_list = table.find_all("tr")[1:]

        if not tr_list and self.page > 2400:
            self.crawler.engine.close_spider(self)

        for tr in tr_list:

            ip_info = IPItem()
            ip_info["host"] = tr.contents[0].text
            ip_info["port"] = tr.contents[1].text

            if Cache.is_exist("{}:{}".format(ip_info["host"], ip_info["port"])):
                continue

            ip_info["proxy_type"] = 0
            ip_info["anonymity_type"] = FieldParser.get_anonymity_type(tr.contents[3].text)
            ip_info["region"] = FieldParser.get_region(tr.contents[2].text)

            try:
                yield ip_info
            except Exception as exc:
                self.logger.error("【程序异常】{}".format(exc))


if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute(['scrapy', 'crawl', '66ip'])
