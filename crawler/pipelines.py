"""数据管道"""

import MySQLdb

from crawler.settings.settings import MYSQL

from utils.cache import Cache

conn = MySQLdb.connect(
    host=MYSQL["host"],
    port=MYSQL["port"],
    user=MYSQL["user"],
    passwd=MYSQL["passwd"],
    db=MYSQL["db"],
    charset=MYSQL["charset"]
)

cursor = conn.cursor()


class IPPipeline:

    @staticmethod
    def process_item(item, spider):

        sql = "insert into api_ip (host, port, proxy_type, anonymity_type, region) values (%s, %s, %s, %s, %s)"

        try:
            cursor.execute(
                sql, [
                    item.get("host"),
                    item.get("port"),
                    item.get("proxy_type"),
                    item.get("anonymity_type"),
                    item.get("region"),
                ]
            )

            conn.commit()

            ip_title = "{}:{}".format(item["host"], item["port"])
            Cache.set(ip_title)
            spider.logger.warning("【导入成功】{}".format(ip_title))

        except Exception as exc:
            spider.logger.error("【导入失败】{}".format(exc))

        return item
