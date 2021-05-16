import scrapy
from bs4 import BeautifulSoup

from crawler.items import IPItem
from utils.cache import Cache
from utils.field_parse import FieldParser


class EightNineIpSpider(scrapy.Spider):
    name = "89ip"
    page = 1

    def start_requests(self):
        while True:

            if self.page == 140:
                break

            url = "http://www.89ip.cn/index_{}.html".format(self.page)
            self.page += 1
            yield scrapy.Request(url)

    def parse(self, response, **kwargs):
        res = response.body

        soup = BeautifulSoup(res, "lxml")
        tbody = soup.find("tbody")

        tr_list = tbody.find_all("tr")

        # if not tr_list:
        #     self.crawler.engine.close_spider(self)

        for tr in tr_list:
            td_list = tr.find_all("td")

            ip_info = IPItem()
            ip_info["host"] = td_list[0].text.strip()
            ip_info["port"] = td_list[1].text.strip()

            if Cache.is_exist("{}:{}".format(ip_info["host"], ip_info["port"])):
                continue

            ip_info["proxy_type"] = 0
            ip_info["anonymity_type"] = 1
            ip_info["region"] = FieldParser.get_region(td_list[2].text.strip())

            try:
                yield ip_info
            except Exception as exc:
                self.logger.error("【程序异常】{}".format(exc))


if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute(['scrapy', 'crawl', '89ip'])
