# import test_hook_assistant
import base64
import hashlib
import random
import time
from urllib.parse import quote_plus

import requests
import rsa
from Crypto.PublicKey import RSA


def md5_after(bArr):
    f10685a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    length = len(bArr)
    cArr = [None] * (length << 1)
    i2 = 0
    for i3 in range(length):
        i4 = i2 + 1
        cArr2 = f10685a
        cArr[i2] = cArr2[(bArr[i3] >> 4) & 15]
        i2 = i4 + 1
        cArr[i4] = cArr2[bArr[i3] & 15]
    return ''.join(cArr)


def gen_sign(sign_ori):
    instance = hashlib.md5()
    instance.update(sign_ori.encode('utf8'))
    dig = instance.digest()
    return md5_after(dig).upper()


def gen_rand():
    str1 = ''
    for i in range(10):
        str1 += str(random.randint(0, 9))
    return str1


def gen_pubkey1():
    p = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDZ2bnVXHfDEJnTic8//BK3Bkm\r2DnraCvnknXdqd+84ZYtRhYA/+MsQWv1k6qH6aR1yXagtnGVZeoO3722fWDtIQFK\regY2LZuADRONNNJC75+WTaHuQfXULXynMGwkkhtXCt0HrGtOVpJ1jP60HrJ4qVYa\rlM+8svZbYNYLqfOsHwIDAQAB"
    return base64.b64decode(p)


def gen_pubkey():
    f16023b = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
               -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55,
               56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
               36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1]
    p = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDZ2bnVXHfDEJnTic8//BK3Bkm\r2DnraCvnknXdqd+84ZYtRhYA/+MsQWv1k6qH6aR1yXagtnGVZeoO3722fWDtIQFK\regY2LZuADRONNNJC75+WTaHuQfXULXynMGwkkhtXCt0HrGtOVpJ1jP60HrJ4qVYa\rlM+8svZbYNYLqfOsHwIDAQAB"
    # p = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCfeke6QsD7GSeu3r+S0fghY4S93CQwq7GQSwx/mf+7bCL0XPweIFKAKYtZ6hXqRxmjmDJbZSl4imWVYZM3dNCbf4kDcthvlhEzR/Jcr/yHi5W1tL+yqBdnnAfcGkMT9tdZl/1sYB+aOMIP4tw07y53zFWtXszz/wCrA/jHopXHNQIDAQAB";

    stringBuffer = ''
    bytes = p.encode('US-ASCII')
    print(len(bytes))
    length = len(bytes)
    i6 = 0

    while i6 < length:
        while True:
            i2 = i6 + 1
            b2 = f16023b[bytes[i6]]
            if (i2 >= length or b2 != -1):
                break

            i6 = i2

        if (b2 == -1):
            break

        while True:
            i3 = i2 + 1
            b3 = f16023b[bytes[i2]]
            if ((i3 >= length) or (b3 != -1)):
                break

            i2 = i3

        if (b3 == -1):
            break

        stringBuffer += chr((b2 << 2) | ((b3 & 48) >> 4))
        while True:
            i4 = i3 + 1
            b6 = bytes[i3]
            if (b6 == 61):
                return stringBuffer.encode('iso8859-1')

            b4 = f16023b[b6]
            if ((i4 >= length) or (b4 != -1)):
                break

            i3 = i4

        if (b4 == -1):
            break

        stringBuffer += chr(((b3 & 15) << 4) | ((b4 & 60) >> 2))
        while True:
            i5 = i4 + 1
            b7 = bytes[i4]
            if (b7 == 61):
                return stringBuffer.encode('iso8859-1')

            b5 = f16023b[b7]
            if (i5 >= length or b5 != -1):
                break

            i4 = i5

        if (b5 == -1):
            break

        stringBuffer += chr(b5 | ((b4 & 3) << 6))
        i6 = i5

    print(stringBuffer)
    print(stringBuffer.encode('iso8859-1'))
    print(stringBuffer.encode('iso8859-1').hex())
    return stringBuffer.encode('iso8859-1')


def encode_rsa(bArr):
    f16022a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+',
               '/']

    stringByffer = ''
    length = len(bArr)
    i2 = 0
    while True:
        if (i2 >= length):
            break

        i3 = i2 + 1
        i4 = bArr[i2] & 255
        if (i3 == length):
            stringByffer += f16022a[i4 >> 2]
            stringByffer += f16022a[(i4 & 3) << 4]
            stringByffer += '=='
            break

        i5 = i3 + 1
        i6 = bArr[i3] & 255
        if (i5 == length):
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

    return stringByffer


def zfillStrToBin(s):
    b = bytes(s.encode())
    for i in range(128 - len(b)):
        b += b'\0'
    print(len(b))
    return b


def gen_enc(pwd):
    # pubkey = gen_pubkey()
    pubkey = gen_pubkey1()
    # rsa_key = RSA.importKey(pubkey)
    # cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    # encrypt_data = cipher.encrypt(pwd.encode('utf8'))
    # return encode_rsa(encrypt_data)

    rsakey = RSA.importKey(pubkey)
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


def star():
    header = {
        "Host": "api.passport.picovr.com",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.11.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": None
    }

    # exports = test_hook_assistant.start_rpc()

    tstp = str(int(time.time() * 1000))
    print('timestamp:', tstp)
    salt = gen_rand()
    salt = '7113922146'
    print('salt:', salt)
    enc_ori = "password=" + "iloveyou" + "&salt=" + salt
    enc = gen_enc(enc_ori)
    # enc = exports.geta(enc_ori)
    print('enc:', enc)
    # enc = 'upazAW3dXRATecpjt0Vw5tjkTsFAZ3KOcYAnUE715aSmbmG/NJNOBkeYicLM/PSbQktfXyq+CCxvF8ddo3pmaXPb8eWs5ddIOpSaaZo/CzyiaNMW1rNc53I3sv4ozgjSlMAp3uvOAXK0K64cLweLczk9Q6ORAODcFQrsg+iqSdE='
    sign_ori = 'apiaccount=vrpuc-aaf91f835147ce2d01216bd3bd5c3516&enc=' + enc + '&phone=15202853541&timestamp=' + tstp + '&key=a0f723c011346j39w049d7bf0356b34b'

    sign = gen_sign(sign_ori)
    print('sign:', sign)

    data = "apiaccount=vrpuc-aaf91f835147ce2d01216bd3bd5c3516&phone=15202853541&sign=" + sign + "&enc=" + quote_plus(
        enc) + "&timestamp=" + tstp

    with requests.session() as session:
        res = session.post(url='http://api.passport.picovr.com/loginUser', headers=header, data=data)
        print(res.text)


star()

# #public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCfeke6QsD7GSeu3r+S0fghY4S93CQwq7GQSwx/mf+7bCL0XPweIFKAKYtZ6hXqRxmjmDJbZSl4imWVYZM3dNCbf4kDcthvlhEzR/Jcr/yHi5W1tL+yqBdnnAfcGkMT9tdZl/1sYB+aOMIP4tw07y53zFWtXszz/wCrA/jHopXHNQIDAQAB";
# private_key = "MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAJ96R7pCwPsZJ67ev5LR+CFjhL3cJDCrsZBLDH+Z/7tsIvRc/B4gUoApi1nqFepHGaOYMltlKXiKZZVhkzd00Jt/iQNy2G+WETNH8lyv/IeLlbW0v7KoF2ecB9waQxP211mX/WxgH5o4wg/i3DTvLnfMVa1ezPP/AKsD+Meilcc1AgMBAAECgYBhuG4HRiw2MN3OG5PMBXlEDFUkeaZ7ZFmzjykjb1vynnp0vh2G4EttWQeYmwW+vr6JLhN9SWm2ASfp9xZcXuoLxAPitW+tVDL6oqaBvDfnvt8sOKn8YrMRQSziT3Kc9bOII8hnoA+0gDCMcuH+NRvdbz9lkaH4/14IsyrT6fSkaQJBAOtMqquZCsrsfvI2jgOtIDFrmE4OM4DegDdBwL8oj+fQdBstFKhdJQnuf3ej3mbku7IAU3XoFYb4RyOH49v+lrcCQQCtgfsPXrBwG+bgd8kYzJR0mfXg2KgqGC0Ek7K0aK5pNvnxPXU0asZfj8UuMo4z+WVVoG26lxrePXQmfZGZbYVzAkEAzoBeWHLb0fN0BcZzJC7QTg8Lf5VfBf4/sD74lctXYC7FdwQ9WPVGCE1TeQBLsymSwEkg9h1UpztF05zzEKOCSQJARhmTw3vwMPs05k+/EaPl/s4NRxCBsLAf0A+UTctVW/D4Pn0kE09oYkeF1MpcJaeHR3cPnilak5ukh8CHyMM0/QJAJ81Ao1NbGRZdgsV7Qzz4B3WS9BANIcGyryyfah/qnevlh9dyVkxxFPAe4BRaeK4qpC28toGtMqGdcwc4arEa4w==";

# #ori_pub = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDZ2bnVXHfDEJnTic8//BK3Bkm\r2DnraCvnknXdqd+84ZYtRhYA/+MsQWv1k6qH6aR1yXagtnGVZeoO3722fWDtIQFK\regY2LZuADRONNNJC75+WTaHuQfXULXynMGwkkhtXCt0HrGtOVpJ1jP60HrJ4qVYa\rlM+8svZbYNYLqfOsHwIDAQAB"


# def decode_pub_key():
#     f16023b = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1]
#     p = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDZ2bnVXHfDEJnTic8//BK3Bkm\r2DnraCvnknXdqd+84ZYtRhYA/+MsQWv1k6qH6aR1yXagtnGVZeoO3722fWDtIQFK\regY2LZuADRONNNJC75+WTaHuQfXULXynMGwkkhtXCt0HrGtOVpJ1jP60HrJ4qVYa\rlM+8svZbYNYLqfOsHwIDAQAB"
#     #p = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCfeke6QsD7GSeu3r+S0fghY4S93CQwq7GQSwx/mf+7bCL0XPweIFKAKYtZ6hXqRxmjmDJbZSl4imWVYZM3dNCbf4kDcthvlhEzR/Jcr/yHi5W1tL+yqBdnnAfcGkMT9tdZl/1sYB+aOMIP4tw07y53zFWtXszz/wCrA/jHopXHNQIDAQAB";

#     stringBuffer = ''
#     bytes = p.encode('US-ASCII')
#     print(len(bytes))
#     length = len(bytes)
#     i6 = 0

#     while i6<length:
#         while True:
#             i2 = i6 + 1
#             b2 = f16023b[bytes[i6]]
#             if (i2 >= length or b2 != -1):
#                 break

#             i6 = i2

#         if (b2 == -1):
#             break

#         while True:
#             i3 = i2 + 1
#             b3 = f16023b[bytes[i2]]
#             if ((i3 >= length) or (b3 != -1)):
#                 break

#             i2 = i3

#         if (b3 == -1):
#             break

#         stringBuffer += chr((b2 << 2) | ((b3&48)>>4))
#         while True:
#             i4 = i3 + 1
#             b6 = bytes[i3]
#             if (b6 == 61):
#                 return stringBuffer.encode('iso8859-1')

#             b4 = f16023b[b6]
#             if ((i4 >= length) or (b4 != -1)):
#                 break

#             i3 = i4

#         if (b4 == -1):
#             break


#         stringBuffer += chr(((b3&15)<<4) | ((b4&60)>>2))
#         while True:
#             i5 = i4 + 1
#             b7 = bytes[i4]
#             if(b7 == 61):
#                 return stringBuffer.encode('iso8859-1')

#             b5 = f16023b[b7]
#             if (i5 >= length or b5 != -1):
#                 break

#             i4 = i5

#         if (b5 == -1):
#             break

#         stringBuffer += chr(b5 | ((b4&3)<<6))
#         i6 = i5

#     print(stringBuffer)
#     print(stringBuffer.encode('iso8859-1'))
#     print(stringBuffer.encode('iso8859-1').hex())
#     return stringBuffer.encode('iso8859-1')


# def generate_salt():
#     salt = ''
#     for i in range(10):
#         salt += str(random.randint(0,9))
#     return salt

# def zfillStrToBin(s):
#     b=bytes(s.encode())
#     for i in range(128-len(b)):
#         b+=b'\0'
#     print(len(b))
#     return b


# def generate_enc():
#     salt = generate_salt()
#     print('salt:',salt)
#     #pwd = "password=" + passwd + "&salt=" + salt
#     pwd = 'password=iloveyou&salt=3103305672'
#     #print('pwd:',pwd)
#     #get rsa pub key
#     pub_key = decode_pub_key()
#     #for i in pwd.encode():
#     #    print(i, end=' ')
#     #print('\n')


#     rsakey = RSA.importKey(pub_key)
#     print('n:',rsakey.n)
#     print('e:',rsakey.e)
#     #获取密钥长度
#     kLen = rsa.common.byte_size(rsakey.n)
#     print('klen:', kLen)
#     #no padding 填充都为0 
#     msg = zfillStrToBin(pwd)
#     _b = rsa.transform.bytes2int(msg)
#     print('_b:',_b)
#     _i = rsa.core.encrypt_int(_b, rsakey.e, rsakey.n)
#     result = rsa.transform.int2bytes(_i, kLen)
#     enc = encode_rsa(result)
#     return enc

#     #RSA.importKey()
#     #rsakey = RSA.importKey(base64.b64decode(ori_pub.encode()))
#     rsakey = RSA.importKey(pub_key)
#     print('ex:',rsakey.exportKey())
#     cipher = Cipher_pkcs1_v1_5.new(rsakey)
#     print('will enc pwd:',pwd.encode())

#     result = cipher.encrypt(pwd.encode())

#     print('result:',result)
#     #enc = str(base64.b64encode(result))
#     enc = encode_rsa(result)
#     print('encr with public result:',enc)
#     return enc

# def do_md5(ori_str):
#     '''
#     com.blankj.utilcode.util.D.a  md5
#     '''
#     instance = hashlib.md5()
#     instance.update(ori_str.encode('utf8'))
#     return instance.digest()

# def encode_md5(bArr):
#     '''
#     bArr:md5后的值
#     com.blankj.utilcode.util.D.q
#     '''
#     f10685a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
#     length = len(bArr)
#     cArr = [None]*(length<<1)
#     i2 = 0
#     for i3 in range(0, length):
#         i4 = i2 + 1
#         cArr2 = f10685a
#         cArr[i2] = cArr2[(bArr[i3] >> 4) & 15]
#         i2 = i4 + 1
#         cArr[i4] = cArr2[bArr[i3]&15]
#     return ''.join(cArr).upper()

# def	encode_rsa(bArr):
#     f16022a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

#     stringByffer = ''
#     length = len(bArr)
#     i2 = 0
#     while True:
#         if (i2 >= length):
#             break

#         i3 = i2 + 1
#         i4 = bArr[i2] & 255
#         if (i3 == length):
#             stringByffer += f16022a[i4 >> 2]
#             stringByffer += f16022a[(i4&3) << 4]
#             stringByffer += '=='
#             break

#         i5 = i3+1
#         i6 = bArr[i3]&255
#         if (i5 == length):
#             stringByffer += f16022a[i4 >> 2]
#             stringByffer += f16022a[((i4&3)<<4) | ((i6&240)>>4)]
#             stringByffer += f16022a[(i6&15) << 2]
#             stringByffer += "="
#             break

#         i7 = i5 + 1
#         i8 = bArr[i5]&255
#         stringByffer += f16022a[i4>>2]
#         stringByffer += f16022a[((i4&3)<<4) | ((i6&240)>>4)]
#         stringByffer += f16022a[((i6&15)<<2)|((i8&192)>>6)]
#         stringByffer += f16022a[i8&63]
#         i2 = i7

#     return stringByffer 		

# def test():
#     str = 'password=iloveyou&salt=5711344821'
#     print('een:',encode_rsa(str.encode()))

# def start():
#     #rpc = test_hook_assistant.start_rpc()
#     passwd = 'iloveyou'
#     tel = '15202853541'
#     enc = generate_enc()
#     #enc = 'VhdV4yib+BcoQdY5J66t976CxusL+L/mR2i7wEIEomd0H3Xk2ula19PCF+7U5ATV1XLk4fuwH4IWlk4Y0Phyd/VoT5KjwzbuxgUhAVg7Ck4tsJ0wbx4RpujlK6vUkgzZ3kyhmt0LZYMbm+KnOF9Ue5dLuoTVzroPxdIQjXIV9OU='
#     #enc = 'Z0NZ16foDyjpY6QaCKUsfYagD/2X1OZgC4k851i/xb0ioavVcuhK8xAE98jthVwYfgf//pVpajobahdLVNuPiLav/UL0jB47Kq2E7xciOTnphq3EQECUAybipSCkDQ+SOz1GYpDgo8DFrsb9v/sr6tYuPHB1lHgqHKIg+RppBgQ='
#     #pub = decode_pub_key()
#     #print('pub:',pub)
#     #enc = rpc.testfunc()
#     #enc = encode_rsa(base64.b64decode(enc))
#     print('enc:'+enc)
#     timestamp = str(int(time.time()*1000))
#     #timestamp = '1632413672082'
#     ori_str = 'apiaccount=vrpuc-aaf91f835147ce2d01216bd3bd5c3516&enc='+enc+'&phone='+tel+'&timestamp='+timestamp+'&key=a0f723c011346j39w049d7bf0356b34b'
#     #ori_str = 'apiaccount=vrpuc-aaf91f835147ce2d01216bd3bd5c3516&enc=Ij892zbKjd3ucK1u3BROe7sl4w4GEVphDbfXX+K6aUYUkTCvz9oAhb6Md/TyC81W16lJCpZpzPv6Jl+f2RKbs3s2RrAVIF6BjVVKDaBl2cn2BQnFxwbcTjYez0hAOKEh63eqXWtyd1/SVEeYGjVq8vyOetRJc20zVdZ/mw40SBk=&phone=15202853541&timestamp=1632413672082&key=a0f723c011346j39w049d7bf0356b34b'
#     sig = do_md5(ori_str)
#     sig = encode_md5(sig)
#     print('sig:',sig)
#     #apiaccount=vrpuc-aaf91f835147ce2d01216bd3bd5c3516&phone=15202853541&sign=8C94089E6A61095B5E866C0FB152B371&enc=lT7gvwMBTtG1mzNas%2FQdkk0gdyP9r3yj1A53xptSIauO5UtctpqDcDOE5pK%2BR%2B7%2Brj5PIhxQm7Vvp%2BIEekj70o8sXGc3QSipSACo7%2FDg81UOg4qwRtpa0R6xFCQ0o%2F5EvKyU%2BxtCKYTXqwmW7AVWsrPA5UAxY8rIlnvneEwaOpU%3D&timestamp=1632283106944

#     header = {
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'User-Agent': 'okhttp/3.11.0',
#         'Accept-Encoding':None,
#         'Accept':None
#     }

#     data = 'apiaccount=vrpuc-aaf91f835147ce2d01216bd3bd5c3516&phone='+tel+'&sign='+sig+'&enc='+quote_plus(enc)+'&timestamp='+ timestamp
#     print('quote enc:',quote_plus(enc))
#     with requests.Session() as session:
#         res = session.post(url='http://api.passport.picovr.com/loginUser', headers=header, data=data)
#         print(res.text)
#         pass

# start()
# #test()
