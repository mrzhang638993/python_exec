import random

# 根据random生成随机数
content = ''
for i in range(0, 10):
    print(i)
    content += str(random.randint(0, 9))
print(content)
