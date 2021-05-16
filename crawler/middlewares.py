from scrapy import signals


class IPCrawlerSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    @staticmethod
    def spider_opened(spider):
        """爬虫启动"""
        spider.logger.warning("【开始执行IP爬取任务】{}".format(spider.name))

    @staticmethod
    def process_start_requests(start_requests, spider):
        """起始请求"""
        for request in start_requests:
            spider.logger.warning("【请求解析中】{}".format(request))
            yield request

    @staticmethod
    def process_spider_input(response, spider):
        return None

    @staticmethod
    def process_spider_output(response, result, spider):

        for i in result:
            yield i

    @staticmethod
    def process_spider_exception(response, exception, spider):
        pass


class IPCrawlerDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    @staticmethod
    def spider_opened(spider):
        pass

    @staticmethod
    def process_request(request, spider):
        spider.logger.warning("【检查请求中数据是否已经爬取过】{}".format(request))
        return None

    @staticmethod
    def process_response(request, response, spider):
        return response

    @staticmethod
    def process_exception(request, exception, spider):
        pass
