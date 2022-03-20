# 模拟assistant的登录操作过程
# 现阶段出现如下的情况:{"ret_msg":"enc解密失败","ret_code":"enc_decrypt_error"} 需要进一步排查enc的数据问题
# 需要大量的熟悉python的库文件等的的信息的。这个才是最重要的内容的。熟悉python的库的开发方式很重要的。
import base64
import hashlib
import random
import time
from urllib.parse import quote_plus

import requests
import rsa
from Crypto.PublicKey import RSA

import assistant


def md5_after(digest):
    f10685a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if digest:
        length = len(digest)
        i2 = 0
        cArr = [None] * (length << 1)
        for i3 in range(length):
            i4 = i2 + 1
            cArr2 = f10685a
            cArr[i2] = cArr2[(digest[i3] >> 4) & 15]
            i2 = i4 + 1
            cArr[i4] = cArr2[digest[i3] & 15]
    return ''.join(cArr)


def gen_sin(sign_ori):
    instance = hashlib.md5()
    instance.update(sign_ori.encode('utf-8'))
    digest = instance.digest()
    cArr = md5_after(digest).upper()
    return "".join(str(cArr))


def star():
    header = {
        "Content-type": "application/x-www-form-urlencoded",
        "Host": "api.passport.picovr.com",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.11.0",
        "Accept": None
    }
    exports = assistant.start_rpc()
    password = "Mrzhang1@"
    con = "password=" + password + "&salt=" + str(getrand())
    timestamp = str(int(time.time() * 1000))
    # 使用frida的export方式调用,避免了构造相关的参数来实施调用的。测试使用构造参数来调用的话，问题很大的。对应的sign也是可以采用如下的方式来调用的。
    # enc = exports.testfunc(con)
    enc = enc_str(password)
    # 直接rpc的方式调用对应的anorid的代码的，不用写代码的
    # rpc的调用还存在一些环境问题的。手机长时间运行的话，对应的也是存在一些问题的。
    print("enc=", enc)
    sign_ori = "apiaccount=vrpuc-aaf91f835147ce2d01216bd3bd5c3516&enc=" + enc + "&phone=13392112455&timestamp=" + timestamp + "&key=a0f723c011346j39w049d7bf0356b34b"
    print("sign_ori=", sign_ori)
    sign = gen_sin(sign_ori)
    print("sign=", sign)
    data = "apiaccount=vrpuc-aaf91f835147ce2d01216bd3bd5c3516&phone=13392112455&sign=" + sign + "&enc=" + quote_plus(
        enc) + "&timestamp=" + timestamp
    print("data=", data)
    with requests.session() as session:
        res = session.post(url="http://api.passport.picovr.com/loginUser", data=data, headers=header)
        print(res.text)


def enc_str(content):
    random = getrand()
    return getenc(content, random)


def getenc(content, random):
    con = "password=" + content + "&salt=" + random
    key = """MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDZ2bnVXHfDEJnTic8//BK3Bkm2DnraCvnknXdqd+84ZYtRhYA/+MsQWv1k6qH6aR1yXagtnGVZeoO3722fWDtIQFKegY2LZuADRONNNJC75+WTaHuQfXULXynMGwkkhtXCt0HrGtOVpJ1jP60HrJ4qVYalM+8svZbYNYLqfOsHwIDAQAB"""
    destkey = bkey(key, con)
    print("destkey=" + destkey)
    return destkey

def  gen_key1():
    p = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDZ2bnVXHfDEJnTic8//BK3Bkm\r2DnraCvnknXdqd+84ZYtRhYA/+MsQWv1k6qH6aR1yXagtnGVZeoO3722fWDtIQFK\regY2LZuADRONNNJC75+WTaHuQfXULXynMGwkkhtXCt0HrGtOVpJ1jP60HrJ4qVYa\rlM+8svZbYNYLqfOsHwIDAQAB"
    return base64.b64decode(p)

# 对应的本质实质是base64解密的过程的，对应的是public的base64解密过程
def gen_key(key):
    f16023b = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
               -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55,
               56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
               36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1]
    buffer = ""
    by1 = key.encode("US-ASCII")
    length = len(by1)
    i6 = 0
    while i6 < length:
        while True:
            i2 = i6 + 1
            b2 = f16023b[by1[i6]]
            if i2 >= length or b2 != -1:
                break
            i6 = i2
        if b2 == -1:
            break
        while True:
            i3 = i2 + 1
            b3 = f16023b[by1[i2]]
            if i3 >= length or b3 != -1:
                break
            i2 = i3
        if b3 == -1:
            break
        buffer += chr((b2 << 2) | ((b3 & 48) >> 4))
        while True:
            i4 = i3 + 1
            b6 = by1[i3]
            if b6 == 61:
                return buffer.encode("iso8859-1")
            b4 = f16023b[b6]
            if i4 >= length or b4 != -1:
                break
            i3 = i4
        if b4 == -1:
            break
        buffer += chr(((b3 & 15) << 4) | ((b4 & 60) >> 2))
        while True:
            i5 = i4 + 1
            b7 = by1[i4]
            if b7 == 61:
                return buffer.encode("iso8859-1")
            b5 = f16023b[b7]
            if i5 >= length or b5 != -1:
                break
            i4 = i5
        if b5 == -1:
            break
        buffer += chr(b5 | ((b4 & 3) << 6))
        i6 = i5
    return buffer.encode("iso8859-1")


def encode_rsa(bArr):
    f16022a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+',
               '/']
    stringByffer = ''
    length = len(bArr)
    i2 = 0
    while True:
        if i2 >= length:
            break
        i3 = i2 + 1
        i4 = bArr[i2] & 255
        if i3 == length:
            stringByffer += f16022a[i4 >> 2]
            stringByffer += f16022a[(i4 & 3) << 4]
            stringByffer += '=='
            break
        i5 = i3 + 1
        i6 = bArr[i3] & 255
        if i5 == length:
            stringByffer += f16022a[i4 >> 2]
            stringByffer += f16022a[((i4 & 3) << 4) | ((i6 & 240) >> 4)]
            stringByffer += f16022a[(i6 & 15) << 2]
            stringByffer += "="
            break
        i7 = i5 + 1
        i8 = bArr[i5] & 255
        stringByffer += f16022a[i4 >> 2]
        stringByffer += f16022a[((i4 & 3) << 4) | ((i6 & 240) >> 4)]
        stringByffer += f16022a[((i6 & 15) << 2) | ((i8 & 192) >> 6)]
        stringByffer += f16022a[i8 & 63]
        i2 = i7
    print("stringByffer=" + stringByffer)
    return stringByffer

#需要进一步的排查安卓的rsa加密存在的问题
#安卓的rsa对应的是默认是不填充的，java等的其他的操作的是默认的填充的。
def bkey(key, pwd):
    pub_key = gen_key(key)
    #pub_key=gen_key1()
    # rsa_key = RSA.importKey(pub_key)
    # cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    # rsa_text = base64.b64encode(cipher.encrypt(pwd.encode("utf8")))
    # print("rsa_text=", bytes.decode(rsa_text))
    # return encode_rsa(rsa_text)
    rsakey = RSA.importKey(pub_key)
    print('n:', rsakey.n)
    print('e:', rsakey.e)
    # 获取密钥长度
    kLen = rsa.common.byte_size(rsakey.n)
    print('klen:', kLen)
    # no padding 填充都为0
    msg = zfillStrToBin(pwd)
    _b = rsa.transform.bytes2int(msg)
    print('_b:', _b)
    _i = rsa.core.encrypt_int(_b, rsakey.e, rsakey.n)
    result = rsa.transform.int2bytes(_i, kLen)
    enc = encode_rsa(result)
    return enc


def zfillStrToBin(s):
    b = bytes(s.encode())
    for i in range(128 - len(b)):
        b += b'\0'
    print(len(b))
    return b


def getrand():
    str1 = ''
    for i in range(10):
        str1 += str(random.randint(0, 9))
    return str1


if __name__ == "__main__":
    star()
