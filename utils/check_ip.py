import requests

from api.models import Ip


class CheckIP(object):
    def __init__(self):
        self.local_ip = requests.get("http://httpbin.org/ip").text  # 本地IP

    @classmethod
    def check_ip(cls, host, port):
        """检测单个IP"""
        ip = {
            "http": "http://{}:{}".format(host, port)
        }

        try:
            target = requests.get("http://httpbin.org/ip", proxies=ip, timeout=3).text

            if cls().local_ip != target:
                return True
        except:
            return

    @classmethod
    def check_ips(cls):
        """IP可用性批量检测"""
        ips = Ip.objects.filter(is_valid=True)

        for ip in ips:
            print("{} is checking".format(ip))
            if cls.check_ip(ip.host, ip.port):
                print("【valid】{}".format(ip))
            else:
                ip.is_valid = False
                ip.save()
