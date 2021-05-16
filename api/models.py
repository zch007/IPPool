"""IP数据库 django orm"""

from django.db import models

from api.enumeration import *


class Ip(models.Model):
    is_valid = models.BooleanField(default=True, verbose_name="是否有效")
    host = models.CharField(max_length=15, verbose_name="服务器地址")
    port = models.CharField(max_length=6, verbose_name="端口号")
    proxy_type = models.SmallIntegerField(choices=proxy_type_choices, default=0, verbose_name="代理类型")
    anonymity_type = models.SmallIntegerField(choices=anonymity_type_choices, default=0, verbose_name="匿名类型")
    region = models.SmallIntegerField(choices=region_choices, default=0, verbose_name="地区")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改日期")

    def __str__(self):
        return "【{}】{}:{}".format(self.get_region_display(), self.host, self.port)
