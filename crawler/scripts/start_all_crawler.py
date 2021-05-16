"""获取到所有的爬虫脚本，依次执行"""

import os

from scrapy import cmdline

files = os.listdir("../../crawler/spiders")

crawlers = [
    _file.split(".")[0]
    for _file in files
    if "__" not in _file
]

for crawler in crawlers:
    cmdline.execute(['scrapy', 'crawl', crawler])

