"""scrapy基础配置"""


BOT_NAME = "crawler"

SPIDER_MODULES = ["crawler.spiders"]
NEWSPIDER_MODULE = "crawler.spiders"

# 配置全局的user-agent
# USER_AGENT = "crawler (+http://www.yourdomain.com)"

# 是否遵循君子协议
ROBOTSTXT_OBEY = False

# Scrapy的最大连接数 (default: 16)
CONCURRENT_REQUESTS = 64

# 配置同一个网站的下载延时 (default: 0)
# DOWNLOAD_DELAY = 3

# 对同一网站支持的最大连接和代理数:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# 是否启用cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# 配置全局默认请求头
# DEFAULT_REQUEST_HEADERS = {
#   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#   "Accept-Language": "en",
# }

# 配置解析器中间件
SPIDER_MIDDLEWARES = {
   "crawler.middlewares.IPCrawlerSpiderMiddleware": 543,
}

# 配置下载器中间件
DOWNLOADER_MIDDLEWARES = {
   "crawler.middlewares.IPCrawlerDownloaderMiddleware": 543,
}

# Enable or disable extensions
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# 配置 item pipelines
ITEM_PIPELINES = {
    "crawler.pipelines.IPPipeline": 300,
}

# 限速相关 (disabled by default)
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"
# REDIRECT_ENABLED = False  # 禁止使用重定向

# 日志报告
# LOG_ENABLED = False
LOG_LEVEL = "WARNING"
