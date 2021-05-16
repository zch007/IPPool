"""检测全部IP的可用性脚本"""

from django.core.management import BaseCommand

from utils.check_ip import CheckIP


class Command(BaseCommand):
    def handle(self, *args, **options):
        CheckIP.check_ips()
