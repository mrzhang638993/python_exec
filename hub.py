import cchardet
import traceback
import requests
import farmhash

from ezpymysql import Connection


class Hub(object):

    def __init__(self):
        self.db = Connection(
            'localhost',
            'crawler',
            'root',
            '123456'
        )

    def hubs(self):
        hubs = ['https://mil.news.sina.com.cn/',
                'https://finance.sina.com.cn/stock/',
                'https://finance.sina.com.cn/fund/',
                'https://finance.sina.com.cn/forex/',
                'https://mobile.sina.com.cn/'
                ]
        return hubs

    def data(self, url):
        try:
            content = requests.get(url)
            if content.status_code == 200:
                coding = cchardet.detect(content.content)
                con = content.content.decode(coding['encoding'])
                return con
        except:
            traceback.print_exc()
            pass

    def mysql(self, urlhash, url, html_lzma):
        sql = "insert into crawler_html(urlhash,url,html_lzma) values(%s,%s,%s)"
        self.db.execute(sql, urlhash, url, html_lzma)

    def query(self, id):
        query = "select *  from crawler_html where id=%s"
        content = self.db.query(query, int(id))
        return content


if __name__ == "__main__":
    hub = Hub()
    urls = hub.hubs()
    for url in urls:
        content = hub.data(url)
        hash = farmhash.hash64(url)
        hub.mysql(hash, url, content)
    record = hub.query(1)
    hub.db.close()
