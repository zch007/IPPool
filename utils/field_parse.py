class FieldParser(object):

    @staticmethod
    def get_proxy_type(string):
        if string.count("http") == 1 and "s" not in string:
            return 1
        elif string.count("http") == 1 and "s" in string:
            return 2

        return 0

    @staticmethod
    def get_anonymity_type(string):
        if "高" in string:
            return 1
        elif "透明" in string:
            return 2

        return 0

    @staticmethod
    def get_region(string):
        china = ["中国", "大陆", "省", "市", "县"]
        hongkong = ["香港", "台湾", "澳门"]
        asia = ["亚洲", "亚太", "印度", "泰国", "菲律宾", "越南", "马来西亚", "俄罗斯", "日本", "韩国"]
        europe = ["欧洲", "阿根廷", "英国", "法国", "德国"]
        america = ["美洲", "美国", "巴西"]
        africa = ["非洲", "叙利亚", "阿富汗", "伊拉克"]

        if any(s in string for s in hongkong):
            return 1
        elif any(s in string for s in china):
            return 0
        elif any(s in string for s in asia):
            return 2
        elif any(s in string for s in europe):
            return 3
        elif any(s in string for s in america):
            return 4
        elif any(s in string for s in africa):
            return 5

        return 6


if __name__ == '__main__':
    print(FieldParser.get_proxy_type("httpsxxxhttp"))
    print(FieldParser.get_proxy_type("httpdsdsd"))
    print(FieldParser.get_proxy_type("htst"))

    print(FieldParser.get_region("中国"))
    print(FieldParser.get_region("中国香港"))
    print(FieldParser.get_region("泰国"))
    print(FieldParser.get_region("欧洲"))
    print(FieldParser.get_region("美国"))
    print(FieldParser.get_region("阿富汗"))
    print(FieldParser.get_region("委内瑞拉"))

