import redis

from crawler.settings import settings


class Cache:
    """缓存器"""
    client = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_PARAMS.get("db")
    )

    @classmethod
    def set(cls, title):
        """以集合的形式添加到redis中"""
        cls.client.sadd("ip_pool", title)

    @classmethod
    def is_exist(cls, title):
        """检查是否爬取过"""
        return cls.client.sismember("ip_pool", title)
