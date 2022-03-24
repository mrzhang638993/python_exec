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


# 图形的腐蚀操作,主要用于二值操作的情况下
def erode(path):
    # 这里面定义了(3,3)的卷积核
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.imread(path)
    # 这里面定义了腐蚀的次数信息的,不同的腐蚀次数的话，腐蚀的区域是会越大的。
    erosion = cv2.erode(img, kernel, iterations=1)
    plt.imshow(erosion)
    plt.show()


# 测试不同的腐蚀次数下面的展示的效果,迭代测试越多的话,对应的腐蚀的效果越明显的。
def iterations(path):
    img = cv2.imread(path)
    kernel = np.ones((20, 20), np.uint8)
    img1 = cv2.erode(img, kernel, iterations=1)
    img2 = cv2.erode(img, kernel, iterations=2)
    img3 = cv2.erode(img, kernel, iterations=3)
    img = [img1, img2, img3]
    res = np.hstack(img)
    cv2.imshow("stack", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 图形的膨胀操作实现,腐蚀操作对原来的对象是有损害的，需要增加膨胀的操作来实现修复损害的作用的。
# 膨胀和腐蚀对应的是一个逆运算的操作的。
def dilate(path):
    img = cv2.imread(path)
    # 执行腐蚀操作,消除多余的元素。
    kernel = np.ones((3, 3), np.uint8)
    erode = cv2.erode(img, kernel)
    # 执行膨胀操作。
    # 定义膨胀的kernel信息
    dialateKernel = np.ones((5, 5), np.uint8)
    dialate = cv2.dilate(erode, dialateKernel, iterations=2)
    plt.imshow(dialate)
    plt.show()


# 定义开运算,可以将腐蚀和膨胀对应的定义在一起,执行相关的操作实现的。
# 开运算对应的会执行如下的操作:先进行腐蚀操作,然后进行膨胀操作实现的。
def open(path):
    img = cv2.imread(path)
    # 定义卷积核操作实现
    kernel = np.ones((3, 3), np.uint8)
    last = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    plt.imshow(last)
    plt.show()


# 执行闭运算操作实现,对应的是首先进行膨胀操作,然后进行腐蚀操作实现的。
def close(path):
    img = cv2.imread(path)
    kernel = np.ones((3, 3), np.uint8)
    last = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    plt.imshow(last)
    plt.show()


# 执行梯度运算操作,梯度运算=膨胀结果-腐蚀结果
# 执行梯度运算的结果实现操作。
def gradient(path):
    img = cv2.imread(path)
    # 定义卷积核的操作实现
    kernel = np.ones((7, 7), np.uint8)
    # 执行梯度计算操作实现
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    plt.imshow(gradient)
    plt.show()


# 对应的执行相关的礼帽的运算和输出操作实现。礼帽的运算结果如下=原始计算结果-开运算的结果
def limao(path):
    img = cv2.imread(path)
    kernel = np.ones((7, 7), np.uint8)
    limao = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    plt.imshow(limao)
    plt.show()


# 执行黑帽运算操作实现
# 对应的黑猫运算的结果是如下的:黑帽运算结果如下=闭运算的计算结果-原始的图形结果
def heimao(path):
    img = cv2.imread(path)
    kernel = np.ones((7, 7), np.uint8)
    heimao = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    plt.imshow(heimao)
    plt.show()


# 执行梯度计算的算子操作实现，在边缘检测的时候，可以使用到这样的方式实现梯度计算操作的。
def sobel(path):
    img = cv2.imread(path)
    # opencv默认的情况下会将负值截断为0的,但是负值是允许的。cv2.CV_64F代表的是将数据转换成为了负数形式的
    # dx=1 代表的是计算水平的梯度，dy=0代表的是计算垂直方向的梯度的。
    # ksize=3代表的是代表的是卷积核的大小的，3*3的卷积核进行操作的。
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    # 下面需要将负数进行绝对值转换的，对应的操作是如下的
    sobelx = cv2.convertScaleAbs(sobelx)
    # 下面计算y方向的相关的梯度运算结果的
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobely = cv2.convertScaleAbs(sobely)
    # 不建议直接计算dx以及dy的数值的，建议分开计算的，那样效果比较的好的。
    # cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3) 对应的是一起计算的操作实现的。
    sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    plt.imshow(sobel)
    plt.show()


# 测试梯度计算的结果操作实现，效果比较优化的那种操作
def sobelfact(path):
    # 加载灰度图片
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # 分别计算dx以及dy方向的边界,得到对应的轮廓图
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobelx = cv2.convertScaleAbs(sobelx)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobely = cv2.convertScaleAbs(sobely)
    sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
    plt.imshow(sobel)
    plt.show()


# 梯度计算的算子scharr，相比较于Sobel算子而言，对应的差异会更加的明显的。可以捕捉到更加丰富的梯度信息的。
def scharr(path):
    # 使用灰度图导入的方式实现操作管理
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
    scharrx = cv2.convertScaleAbs(scharrx)
    scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)
    scharry = cv2.convertScaleAbs(scharry)
    scharr = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
    plt.imshow(scharr)
    plt.show()


# 对应的体现的是laplacian梯度计算的方式的，对应的laplacian需要结合其他的方式来实现精准的梯度计算的。
def laplacian(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    lap = cv2.Laplacian(img, cv2.CV_64F)
    lap = cv2.convertScaleAbs(lap)
    plt.imshow(lap)
    plt.show()


# 执行边缘检测算法操作,边缘检测算法操作,canny是一整套的完整的解决方案的。
# 对应的边界的范围设置的越大的话，对应的细节是越清晰的。范围越小的话，对应的细节是会越概略的。
# canny的边缘检测主要包括了如下的多个步骤的：
'''
步骤1: 使用高斯滤波器进行滤波处理，平滑头像，降低噪声
步骤2：计算图像中的每一个像素点的梯度强度和反向
步骤3：使用非极大值抑制，以消除边缘检测所带来的杂散效应
步骤4：使用双阈值确定真实和潜在的边缘
步骤5：通过抑制孤立的弱边缘最终完成边缘检测
'''


def canny(path):
    img = cv2.imread(path)
    # 设置上限和下限值,设置的上限值以及下限值是比较的大的
    can1 = cv2.Canny(img, 80, 150)
    # 设置的下限值是比较的大的
    can2 = cv2.Canny(img, 50, 150)
    plt.imshow(can1)
    plt.show()
    plt.imshow(can2)
    plt.show()


# 使用更大范围的图片来实现相关的数据的canny数据探测操作实现的
def cannyfact(path):
    img = cv2.imread(path)
    can1 = cv2.Canny(img, 120, 250)
    # 设置的下限值是比较的大的
    can2 = cv2.Canny(img, 50, 150)
    plt.imshow(can1)
    plt.show()
    plt.imshow(can2)
    plt.show()


# 图像金字塔的上采样以及下采样操作实现
'''
需要注意的是在上采样的过程中以及下采样的过程中，
对应的都是会损失相关的精度的数据的。所以，不存在经历过一次上下采样之后，对应的不丢失数据的过程的。
过程中都是会存在信息的丢失的过程的。
'''


def pyr(path):
    img = cv2.imread(path)
    # 执行金字塔的上采样操作实现
    pyrUp = cv2.pyrUp(img)
    # 执行金字塔的下采样操作实现
    pyrDown = cv2.pyrDown(img)
    cv_show(pyrUp)
    cv_show(pyrDown)
    # 对应的继续执行上采样的操作实现的
    pyrUpnext = cv2.pyrUp(pyrUp)
    cv_show(pyrUpnext)


# 定义展示的方法
def cv_show(img):
    plt.imshow(img)
    plt.show()


'''
定义拉普拉斯金字塔实现相关的图像的操作处理实现,
对应的是先执行down操作，后续执行up操作的。
比较初始的推行和后续的一套down-up之后的结果的
单一层次的计算是这样的，但是多层次的话，是不同的，需要进行关注的。
可以抽取不同层次的有价值的东西的，可以实现多个层次不同的价值的融合操作的。
'''


def pyrlapu(path):
    img = cv2.imread(path)
    down = cv2.pyrDown(img)
    up = cv2.pyrUp(down)
    dest = img - up
    plt.imshow(dest)
    plt.show()


# 轮廓检测操作实现，轮廓相教于边缘检测而言，需要的是完整性的相关的内容的。
def contours(path):
    img = cv2.imread(path)
    # 转换成为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 使用阈值操作，转化成为二值图，0和255的那种，得到二值图操作
    ret, thrsh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # 下面使用二值图执行边缘检测操作实现，使用边缘检测操作的话，对应的是需要二值图的。这个是关键的信息的
    binary, counters, hierarchy = cv2.findContours(thrsh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # 执行copy操作，否则的话，对应的原图会修改相关的内容的,如果不拷贝的话，是会在原始图上不断的修改的
    img_copy = img.copy()
    # counters对应的是shape信息的，是一个数组的。-1代表的是将所有的轮廓全部展示的。0, 0, 255对应的是bgr的颜色的模式的，对应的是红色的。2代表的是颜色的宽度
    counter = cv2.drawContours(img_copy, counters, -1, (0, 0, 255), 2)
    plt.imshow(counter)
    plt.show()
    # 指定特定的轮廓，开始计算相关的轮廓的特征信息的.对于轮廓的话，是需要根据索引来获取的。
    cnt = counters[0]
    # 计算轮廓的面积
    area = cv2.contourArea(cnt)
    print(area)
    # 计算轮廓的周长
    length = cv2.arcLength(cnt, True)
    print(length)


# 执行轮廓的近似操作实现和管理实现
def approx(path):
    img = cv2.imread(path)
    # 转换成为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 使用阈值操作，转化成为二值图，0和255的那种，得到二值图操作
    ret, thrsh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # 下面使用二值图执行边缘检测操作实现，使用边缘检测操作的话，对应的是需要二值图的。这个是关键的信息的
    binary, counters, hierarchy = cv2.findContours(thrsh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # 执行copy操作，否则的话，对应的原图会修改相关的内容的,如果不拷贝的话，是会在原始图上不断的修改的
    img_copy = img.copy()
    # 对应的代表的是需要处理的轮廓的特征和参数信息
    cnt = counters[0]
    # 对应的是轮廓特征的提取操作实现
    # res = cv2.drawContours(img_copy, [cnt], -1, (0, 0, 255), 2)
    # plt.imshow(res)
    # plt.show()
    # 下面进行轮廓特征的近似操作实现
    epsilon = 0.1 * cv2.arcLength(cnt, True)
    # approx代表的是轮廓的特征信息的，使用的是近似的轮廓的操作实现的。
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    res = cv2.drawContours(img_copy, [approx], -1, (0, 0, 255), 2)
    plt.imshow(res)
    plt.show()
    # 还可以对应的形成外接矩形，外接圆等的图形的
    x, y, w, h = cv2.boundingRect(cnt)
    # 构造外接矩形和相关的内容
    copy1 = img.copy()
    tangle = cv2.rectangle(copy1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    plt.imshow(tangle)
    plt.show()
    # 计算轮廓矩形和外接矩形的面积的对比操作和实现
    # 计算轮廓的面积
    area = cv2.contourArea(cnt)
    # 获取外接矩形的数据信息
    x, y, w, h = cv2.boundingRect(cnt)
    react_area = w * h
    extent = float(area) / react_area
    print("轮廓面积和边界矩形面积之比", extent)


# opencv中的模板匹配方式和操作实现,文件的缺失报错了，后续需要关注统一的异常处理操作。
def templatematch(imgpath, remplatepath):
    # 读取图片操作
    img1 = cv2.imread(imgpath)
    # 读取相关的模板操作实现
    template = cv2.imread(remplatepath)
    # 得到图形的shape数据信息
    h, w = template.shape[:2]
    # 执行模板匹配操作实现
    res = cv2.matchTemplate(img1, template, cv2.TM_SQDIFF_NORMED)
    # 执行对应的查找操作实现
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # 匹配到了位置的话，后续的需要进行相关的数据匹配操作实现管理
    bottom = (min_loc[0] + w, min_loc[1] + h)
    img_copy = img1.copy()
    # 绘制矩形执行操作实现
    tangle = cv2.rectangle(img_copy, min_loc, bottom, 255, 2)
    plt.imshow(tangle)
    plt.show()


# 人脸检测一般的使用机器学习的算法来实现的。不会使用到opencv来执行操作的。
# 其他的几种模板匹配操作和比较
def templatematchall(imgpath, remplatepath):
    # 读取图片操作
    img1 = cv2.imread(imgpath)
    # 读取相关的模板操作实现
    template = cv2.imread(remplatepath)
    # 得到图形的shape数据信息
    h, w = template.shape[:2]
    methods = [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF, cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
               cv2.TM_CCORR_NORMED]
    for method in methods:
        # 执行模板匹配操作实现
        res = cv2.matchTemplate(img1, template, cv2.TM_SQDIFF_NORMED)
        # 执行对应的查找操作实现
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if method in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom = (top_left[0] + w, top_left[1] + h)
        img_copy = img1.copy()
        tangle = cv2.rectangle(img_copy, top_left, bottom, 255, 2)
        plt.imshow(tangle)
        plt.show()


# 模板的多匹配操作实现。多匹配操作的话，需要使用到阈值实现相关的操作的。
def multimatch(imgpath, templatepath):
    img = cv2.imread(imgpath)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(templatepath, 0)
    # 得到图形的shape数据信息
    h, w = template.shape[:2]
    # 计算相关的系数，系数越高的，对应的匹配程度越高的。
    res = cv2.matchTemplate(grey, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    # *代表的是可选的参数,对应的是进行数组的大量的匹配操作的。
    for pt in zip(*loc[::-1]):
        bottom_right = (pt[0] + w, pt[1] + h)
        cv2.rectangle(img, pt, bottom_right, (255, 0, 0), 2)
    plt.imshow(img)
    plt.show()


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
    # flat("C:\\Users\\mrzhang\\2022\\lenaNoise.png")
    # erode("C:\\Users\\mrzhang\\2022\\dige.png")
    # iterations("C:\\Users\\mrzhang\\2022\\pie.png")
    # dilate("C:\\Users\\mrzhang\\2022\\dige.png")
    # open("C:\\Users\\mrzhang\\2022\\dige.png")
    # close("C:\\Users\\mrzhang\\2022\\dige.png")
    # gradient("C:\\Users\\mrzhang\\2022\\pie.png")
    # limao("C:\\Users\\mrzhang\\2022\\dige.png")
    # heimao("C:\\Users\\mrzhang\\2022\\dige.png")
    # sobel("C:\\Users\\mrzhang\\2022\\pie.png")
    # sobelfact("C:\\Users\\mrzhang\\2022\\lena.jpg")
    # scharr("C:\\Users\\mrzhang\\2022\\lena.jpg")
    # laplacian("C:\\Users\\mrzhang\\2022\\lena.jpg")
    # canny("C:\\Users\\mrzhang\\2022\\lena.jpg")
    # cannyfact("C:\\Users\\mrzhang\\2022\\car.png")
    # pyr("C:\\Users\\mrzhang\\2022\\AM.png")
    # pyrlapu("C:\\Users\\mrzhang\\2022\\AM.png")
    # contours("C:\\Users\\mrzhang\\2022\\contours.png")
    # approx("C:\\Users\\mrzhang\\2022\\contours2.png")
    # templatematch("C:\\Users\\mrzhang\\2022\\lena.jpg", "C:\\Users\\mrzhang\\2022\\face.jpg")
    # templatematchall("C:\\Users\\mrzhang\\2022\\lena.jpg", "C:\\Users\\mrzhang\\2022\\face.jpg")
    multimatch("C:\\Users\\mrzhang\\2022\\mario.jpg", "C:\\Users\\mrzhang\\2022\\mario_coin.jpg")
