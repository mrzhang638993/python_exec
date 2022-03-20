import hashlib
import time

content = 'IMEI867980020108911-IMSI460NNNNNNNNNNNN&&1639051134&&f1190aca-d08e-4041-8666-29931cd89dde'
sig = ""
inst = hashlib.md5()
inst.update(bytearray(content.encode('utf8')))
dig = inst.digest()
for i in dig:
    sig = sig + format((i >> 4) & 15, 'x') + format(i & 15, 'x')
print("sig="+sig)
print(sig.__eq__('418a4ebda2591ead2b694cc3061042d7'))
