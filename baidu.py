import requests
# 检测文本的编码格式
import chardet
# 另外的识别软件
import cchardet

#r=requests.get("http://www.baidu.com")
#print(r.encoding)
#print(r.text)
# 二进制代码相关问题
#print(r.content)
# 探测对应的文本的字符集
#print(chardet.detect(r.content))
#print(r.content.decode('utf8'))
#  中文字符集的对应的关系 gb2312<gbk>gn18030 chardet探测的时候可能将对应的gbk探测为gb2312的。存在缺陷的
# 字符识别的另外的一个jar文件操作
print(cchardet.detect('科技健康'.encode('gbk')))
print(cchardet.detect('科技健康几十块访问'.encode('gbk')))
# gbk 探测为gb2312 对应的数据范围降低了，推荐使用cchardet实现数据的探测发现的。
print(chardet.detect('科技健康几十块访问'.encode('gbk')))
#  建议将网页爬取到的原始数据也是需要存储起来的。存储生数据的话，可以防止后续需求发生变化，需要重新爬取的。需要压缩存储的。
# chrome调试的过程对应的就是一个逆向代码的过程的。









