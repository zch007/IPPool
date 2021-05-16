"""各API实现逻辑"""

import json
import random

from django.http import HttpResponse
from django.shortcuts import render

from api.models import Ip


def get_ip_list():
    """获取IP列表"""
    ips = Ip.objects.filter(is_valid=True)

    ip_list = [
        {
            "host": ip.host,
            "port": ip.port,
            "proxy_type": ip.get_proxy_type_display(),
            "anonymity_type": ip.get_anonymity_type_display(),
            "region": ip.get_region_display(),
            "record_time": str(ip.create_time.strftime("%Y-%m-%d %H:%M:%M"))
        }
        for ip in ips
    ]

    return ip_list


def get_count(request):
    """获取可用IP的数量"""
    count = Ip.objects.filter().count()
    valid_count = Ip.objects.filter(is_valid=True).count()

    return HttpResponse("the count of ip in IPPool is {}, but {} is valid!".format(count, valid_count))


def get_ip_by_num(request):
    """随机获取 num 条IP"""
    num = int(request.GET.get("num", 1))
    ip_list = get_ip_list()
    num = len(ip_list) if num > len(ip_list) else num
    ips = random.sample(ip_list, num)

    return HttpResponse(json.dumps(ips), content_type="application/json")


def delete_ip(request):
    """
    删除指定IP
    request中的 id 字段形如 144.232.45.92:80
    """
    ip = str(request.GET.get("ip", "0:0"))
    ip_parse = ip.split(":")
    host = ip_parse[0]
    port = ip_parse[1]

    try:
        deleted_ip = Ip.objects.get(host=host, port=port)
        deleted_ip.is_valid = False
        deleted_ip.save()
        response = "delete {} OK".format(ip)
    except:
        response = "can't find this ip"

    return HttpResponse(response)


def ip_show(request):
    """以网页的形式展示IP"""
    ips = get_ip_list()
    return render(request, "show.html", {"ips": ips})
