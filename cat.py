import cv2
import matplotlib.pyplot as plt
import numpy as np


# 图片对应的是BGR的显示操作的。
# opencv的展示需要其他的方式实现相关的数据展示操作的，可以借助于
# import matplotlib.pyplot as plt 可以借助于这个来实现相关的操作
# 定义读取彩色图的方法
# 对应的是opencv最基本的操作实现的。
def cv_show(path, name, flags=None):
    img = cv2.imread(path, flags)
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 图片保存操作
    # cv2.imwrite("cat1.jpg", img, None)


def tv_show(path, name, flags=None):
    video = cv2.VideoCapture(path)
    if video.isOpened():
        # 如果可以正常的打开的话，open对应的是true,frame对应的是图片的
        open, frame = video.read()
    else:
        open = False
    while open:
        # ret对应的是布尔值的。
        ret, frame = video.read()
        # frame对应的是数组结构的，不能直接使用 if frame来执行操作的。
        if frame is None:
            break
        else:
            # frame对应的是图片的
            if ret:
                # 转换成为灰度图,对应的是图片的相关的操作的
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # 显示图片执行相关的操作
                cv2.imshow(name, gray)
                if cv2.waitKey(10) and 0XFF == 27:
                    break
            else:
                break
    video.release()
    cv2.destroyAllWindows()


# 截取部分感兴趣的数据
def roi(path, name):
    img = cv2.imread(path)
    cat = img[0:200, 0:200]
    # 执行rmi操作，获取得到部分想要的,感兴趣的操作区域
    cv2.imshow(name, cat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 执行颜色提取操作和实现
def get(path):
    img = cv2.imread(path)
    # 执行图片的split操作实现
    b, g, r = cv2.split(img)
    print(g.shape)
    # 执行图片的split切割获取操作实现
    img1 = cv2.merge((b, g, r))
    cv2.imshow("imag1", img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 对应的只是显示部分的通道数据信息
def r(path, name):
    img = cv2.imread(path)
    # 只是包括图片的R通道的数据
    img[:, :, 0] = 0
    img[:, :, 1] = 0
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def g(path, name):
    img = cv2.imread(path)
    # 只是包括图片的G通道的数据
    img[:, :, 0] = 0
    img[:, :, 2] = 0
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def b(path, name):
    img = cv2.imread(path)
    # 只是包括图片的G通道的数据
    img[:, :, 1] = 0
    img[:, :, 2] = 0
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 卷积操作对应的是特征提取操作实现的。
# 执行边界的填充操作实现
def full(path):
    top, bottom, left, right = (50, 50, 50, 50)
    img = cv2.imread(path)
    # 复制法进行填充操作,直接复制最边缘的像素操作实现。
    img1 = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REPLICATE)
    # 反射法进行数据填充操作
    img2 = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REFLECT)
    # 反射法操作实现
    img3 = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REFLECT101)
    # 外包装法操作实现
    img4 = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_WRAP)
    # 常量法，拿常量值进行数据填充操作
    img5 = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=0)


# 执行数值计算操作实现
def calc():
    cat = cv2.imread("C:\\Users\\mrzhang\\2022\\cat.jpg")
    dog = cv2.imread("C:\\Users\\mrzhang\\2022\\dog.jpg")
    # opencv对应的底层是bgr格式要求的数据的。+10代表的是对所有的b,g,r对应的数组都是执行相关的+10的操作实现的
    # cat1 = cat + 10
    # 最终的结果是对应的bgr的数据%256取余得到的数据信息的，备注：shape数值不同的是不能直接相加操作的。不同的shape值相关的话会报错的。
    # cat2 = cat + cat1
    # cv2对应的也是提供了相关的加法的执行的操作实现的,对应的执行原则是如下的。大于255的话，对应的取值255，没有达到255的话，获取和值
    # cat3 = cv2.add(cat, cat1)
    # cv2.imshow("newCat", cat3)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # 不同的shape的话，是不能直接相加的，对应的会报错的。
    # cat+dog
    # 不同的shape的话，对应的需要相关的resize操作实现的。
    # print(cat.shape)  # (414, 500, 3)
    # print(dog.shape)  # (429, 499, 3)
    # 方式一:写出具体的数值执行操作
    # dog = cv2.resize(dog, (500, 414))
    # cat = cat + dog
    # 方式二: 按照x,y对应的方向上的倍数来执行相关的操作实现
    # dog = cv2.resize(dog, (0, 0), fx=3, fy=1)
    # 和上面的一样的操作
    # dog = cv2.resize(dog, (0, 0), fx=1.5, fy=1.5)
    # 对应的实现相关的偏值项来实现相关的操作,对应的计算公式是如下的：0.4*cat+0.6*dog+0
    # 需要注意的是矩阵大小不一致的话，是不能执行加减操作的
    # 需要注意的是在执行addWeighted的时候需要确保两者的bgr是一样的
    dog = cv2.resize(dog, (500, 414))
    res = cv2.addWeighted(cat, 0.4, dog, 0.6, 0)
    # plt.subplot(2, 2, 1)
    plt.imshow(res)
    plt.show()


# 对应的形成相关的阈值函数操作实现和管理替代操作
def threshold(path):
    img = cv2.imread(path)
    # 规则如下:大于127的对应的取值255，小于277的对应的取值0
    ret1, thresd1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # 规则如下:大于127的对应的取值0，小于277的对应的取值255
    ret2, thresd2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    # 大于阈值的设置为阈值，小于阈值的对应的是自身的
    ret3, thresd3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    # 大于阈值部分不变，小于阈值不部分设置为0
    ret4, thresd4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    # 小于阈值部分的不变，大于阈值的设置为0
    ret5, thresd5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
    titles = ["origin_image", "binary", "binary_inv", "tozero", "tozero_inv"]
    cats = [img, thresd1, thresd2, thresd3, thresd4, thresd5]
    for i in range(5):
        plt.subplot(2, 3, i + 1)
        plt.imshow(cats[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()


# 执行图像的平滑操作处理实现,对应的可以执行相关的滤波操作实现
def flat(path):
    img = cv2.imread(path)
    # 执行滤波操作处理实现,对应的（3,3）体现的是滤波操作处理实现
    # 卷积操作,对应的是均值滤波的一种实现。
    blur = cv2.blur(img, (3, 3))
    # 方框滤波操作实现，-1表示和颜色通道一直的，normalize对应的代表的是归一化的操作的
    # 方差滤波以及均值滤波差别的一点对应的是归一化的操作的，配置参数体现的是normalize=True,当配置成为这样的时候，是一样的。
    # 如果normalize=false的，对应的如果大于255的话，对应的都是会设置成为255的
    # blur = cv2.boxFilter(img, -1, (3, 3), normalize=True)
    # 下面对应的是高斯滤波的方式和实现的。对应的是根据高斯分布来实现补偿的，符合高斯分布操作的。
    gause = cv2.GaussianBlur(img, (5, 5,), 1)
    # 执行中值滤波操作实现
    mediam = cv2.medianBlur(img, 5)
    # 使用numpy一次打印多个数据,可以进行效果的比对操作实现和管理的。
    img = [blur, gause, mediam]
    res = np.hstack(img)
    print(res)
    # plt.imshow(blur)
    # plt.show()


if __name__ == "__main__":
    # 读取彩色图片操作实现
    # cv_show("C:\\Users\\mrzhang\\2022\\cat.jpg", "cat",cv2.IMREAD_COLOR)
    # 读取灰度图片操作,需要经常的进行灰度图和彩色图的之间的转换操作的。
    # cv_show("C:\\Users\\mrzhang\\2022\\cat.jpg","cat",cv2.IMREAD_GRAYSCALE)
    # 人脸识别的技术也是基于对应的图片识别技术来实现相关的操作实现的。
    # tv_show("C:\\Users\\mrzhang\\2022\\test.mp4", "hello")
    # roi("C:\\Users\\mrzhang\\2022\\cat.jpg", "hello")
    # get("C:\\Users\\mrzhang\\2022\\cat.jpg")
    # r("C:\\Users\\mrzhang\\2022\\cat.jpg", "cat")
    # b("C:\\Users\\mrzhang\\2022\\cat.jpg", "cat")
    # g("C:\\Users\\mrzhang\\2022\\cat.jpg", "cat")
    # calc()
    # threshold("C:\\Users\\mrzhang\\2022\\cat.jpg")
    flat("C:\\Users\\mrzhang\\2022\\lenaNoise.png")
