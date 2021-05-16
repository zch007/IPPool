"""scrapy线上配置"""

# 配置redis
REDIS_HOST = ""
REDIS_PORT = 6379
REDIS_PARAMS = {
    "db": 1
}

# 配置mysql
MYSQL = {
    "db": "",
    "user": "",
    "passwd": "",
    "host": "",
    "port": 3306,
    "charset": "",
}
