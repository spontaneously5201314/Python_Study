class Cat:
    # 属性

    # 初始化方法，在实例化对象的时候调用
    def __init__(self, name):
        self.name = name
        print("正在实例化")

    # 方法
    def eat(self):  # 实例方法　self就是指最终的实例对象
        print("我的{}猫正在吃东西".format(self.name))
        return 1

    def div(self, a, b):
        try:
            print(a / b)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    my_cat = Cat("tom")  # 实例化一个对象
    result = my_cat.eat()
    print(result)
    my_cat.div(3, 0)
