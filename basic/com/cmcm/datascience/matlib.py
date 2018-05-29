from matplotlib import pyplot
import random


def random_temp():
    temp = []
    for i in range(12):
        temp.append(random.randint(0, 30))
    return temp


if __name__ == '__main__':
    y = random_temp()
    x = list(range(2, 26, 2))
    # figure图形图标的意思,在这里指的就是我们画的图,通过实例化一个figure并传递参数,能够在后台自动使用该figure实例
    # 在图像模糊的时候可以传入dpi参数,让图片更加清晰
    fig = pyplot.figure(figsize=(20, 8), dpi=80)
    pyplot.plot(x, y)
    # 固定x轴上面的数据为我们生成的数据,设置x的刻度
    pyplot.xticks(x)
    # 当刻度太密集的时候,可以使用列表的步长(间隔取值)来解决,matplotlib会自动帮我们对应
    # pyplot.xticks(x[::2])
    # 保存图片,可以保存为svg这种矢量图格式,放大不会有锯齿
    pyplot.savefig("./sig_size.png")
    pyplot.show()
