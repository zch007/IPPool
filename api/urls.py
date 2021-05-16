"""Django服务器API路由配置"""

from django.urls import path

from api import views

app_name = "api"

urlpatterns = [
	path("count/", views.get_count),
	path("get_ip/", views.get_ip_by_num),
	path("delete_ip/", views.delete_ip),
	path("ip_show/", views.ip_show)
]