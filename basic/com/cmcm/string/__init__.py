# input输入的东西在接受到之后都变成字符串了，如果想要变成int，可以使用int(a)
# {}是占位符
print("spon{}".format("taneously"))
# 有两个占位符，后面的format需要传入两个参数
print("{}on{}".format("sp", "taneously"))
# strip方法可以去除掉字符串两边的空格，类似java中的trim，在爬虫中可能会使用到
print(" spontaneously ".strip())
f = "spontaneously"
# 判断某个字符在不在字符串中，返回值是boolean类型，但是第一个字母是大写的
print("s" in f)
