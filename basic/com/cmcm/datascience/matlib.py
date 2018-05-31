from matplotlib import font_manager  # 解决中文问题
from matplotlib import pyplot
import matplotlib  # 解决中文问题
import random


# windows下面的操作
def win_modified_font():
    font = {'family': 'monospace',
            'weight': 'bold',
            'size': 'larger'}
    matplotlib.rc('font', **font)


# linux下面的操作,但是这个方法的返回值需要在xticks方法中传入作为参数才能生效
def linux_modified_font():
    return font_manager.FontProperties(fname="/usr/share/fonts/truetype/arphic/ukai.ttc")


def random_temp():
    temp = []
    for i in range(12):
        temp.append(round(random.uniform(0, 30), 2))
    return temp


# 画折线图
def figure():
    y1 = random_temp()
    y2 = random_temp()
    x = list(range(2, 26, 2))
    # figure图形图标的意思,在这里指的就是我们画的图,通过实例化一个figure并传递参数,能够在后台自动使用该figure实例
    # 在图像模糊的时候可以传入dpi参数,让图片更加清晰
    fig = pyplot.figure(figsize=(20, 8), dpi=80)
    # label用来后面添加图例
    pyplot.plot(x, y1, color="red", linestyle=":", label="y1")
    pyplot.plot(x, y2, color="orange", linestyle="-.", label="y2")
    pyplot.legend(loc="best")
    # 固定x轴上面的数据为我们生成的数据,设置x的刻度
    pyplot.xticks(x, ["{}hour".format(i) for i in range(2, 26, 2)])
    # 当刻度太密集的时候,可以使用列表的步长(间隔取值)来解决,matplotlib会自动帮我们对应
    # pyplot.xticks(x[::2])
    # 保存图片,可以保存为svg这种矢量图格式,放大不会有锯齿
    pyplot.savefig("./sig_size.png")
    # matplotlib默认不支持中文字符,因为默认的英文字体无法显示防止
    # 查看linux下面支持的字体:
    # fc-list 查看支持的字体
    # fc-list :lang=zh 查看支持的中文(注意冒号前面有空格)
    # 如何修改matplotlib的默认字体?
    # 通过matplotlib.rc可以修改,具体方法参加源码
    # 通过matplotlib下的font-manager可以解决
    pyplot.xlabel("time")
    pyplot.ylabel("temp")
    pyplot.title("temp per time")
    # 设置网格
    pyplot.grid(True, alpha=0.3)
    pyplot.show()


def get_random():
    # help(random.uniform)
    return round(random.uniform(3, 20), 2)


# 绘制散点图
def scatter():
    pyplot.figure(figsize=(18, 8), dpi=80)
    pyplot.scatter(list(range(2, 26, 2)), random_temp(), label="three")
    pyplot.scatter(list(range(42, 66, 2)), random_temp(), label="ten")
    pyplot.legend(loc="best")
    pyplot.show()


# 绘制条形图
def bar():
    # pyplot.bar(list(range(2, 26, 2)), random_temp(), width=0.2, color="orange")
    # 颠倒x轴和y轴
    pyplot.barh(list(range(2, 26, 2)), random_temp(), height=0.2, color="orange")
    pyplot.show()


if __name__ == '__main__':
    # figure()
    # print(get_random())
    # scatter()
    bar()
# 1.应该选择哪种图形来呈现数据
# 2.pyplot.plot(x,y)
# 3.pyplot.bar(x,y)
# 4.pyplot.scatter(x,y)
# 5.xticks和yticks的设置
# 6.label和title,grid的设置
# 7.绘图的大小和保存图片
