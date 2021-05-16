## IPPool

### 目录结构:
```markdown
IPPool
···api                           提供各种功能接口
   ···management
      ···commands                用于Django识别命令脚本
···backend                       Django服务器的一些配置
···crawler                       scrapy爬虫框架
   ···scripts                    用于存放爬虫自定义脚本
   ···settings                   scrapy的一些配置
   ···spiders                    存放各个网站的爬虫脚本
   ···templates                  用于存放HTML资源
···utils                         工具类包 提供一些经常复用的方法

```

### 命令:

~~~markdown
执行某一IP网站的爬取: scrapy crawl xxx (xxx代表需要爬取的爬虫脚本名)
          如 scrapy crawl 66ip
          ... ...
执行全部网站的爬取: python crawler/scripts/start_all_crawler.py
IP可用性筛选: python manage.py check_ips
~~~
```markdown
API 服务器启动: python manage.py runserver

获取IP数量: 127.0.0.1/api/count
随机获取IP: 127.0.0.1/api/get_ip?num=10  ?num=10代表获取10条 不带参数代表获取1条
删除指定IP: 127.0.0.1/api/delete_ip?ip=108.45.221.96:8080  代表删除服务器为108.45.221.96, 端口号为8080的这条IP

```