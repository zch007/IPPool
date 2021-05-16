"""models枚举类型"""

proxy_type_choices = (
    (0, "http/https"),
    (1, "http"),
    (2, "https")
)

anonymity_type_choices = (
    (0, "普通匿名"),
    (1, "高匿代理"),
    (2, "透明代理")
)

region_choices = (
    (0, "大陆"),
    (1, "香港"),
    (2, "亚洲"),
    (3, "欧洲"),
    (4, "美洲"),
    (5, "非洲"),
    (6, "其他")
)