#  将新浪新闻首页的新闻和链接爬取出来存到mysql数据库中

import requests
import cchardet
import traceback
from lxml import etree
from ezpymysql import Connection


class XinlangDb(object):

    def __init__(self):
        self.db = Connection(
            'localhost',
            'crawler',
            'root',
            '123456'
        )

    def data(self):
        try:
            r = requests.get('https://news.sina.com.cn/')
            encoding = cchardet.detect(r.content)
            html = r.content.decode(encoding['encoding'])
            tree = etree.HTML(text=html, parser=etree.HTMLParser())
            alist = tree.xpath('//a')
            dict = {}
            for anode in alist:
                arrdict = anode.attrib
                if arrdict.has_key('href') and anode.text != None and arrdict['href'].find('javascript') == -1:
                    dict[anode.attrib['href']] = anode.text
                else:
                    pass
            return dict
        except :
            print("未知异常")
            traceback.print_exc()

    # 爬取到相关的数据,数据存储到对应的mysql数据库中
    def mysql(self, source):
        sql = "insert into crawler_origin_url(url,descs) values(%s,%s)"
        for key, value in source.items():
            self.db.execute(sql, key, value)
        self.db.close()
