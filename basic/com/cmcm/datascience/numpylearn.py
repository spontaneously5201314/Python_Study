# 学习使用numpy
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array(range(6))
c = np.arange(6)
print("a=", a, ",b=", b, ",c=", c)
print(a.dtype)  # 查看数组的类型
# b.dtype
# 创建一个二维数组
t = np.array([[1, 2, 3], [4, 5, 6]])
print(t)
# 返回数组的行和列的数量,返回的是一个元组
# 如果一个元组中只有一个元素,需要加上一个逗号,不然就变成一个数字了
# print(t.shape)
# 将多维数据展开成一维的
print(t.flatten())
print(np.arange(100, 112).reshape(3, 4))

# pandas比numpy好在可以处理字符串和时间序列
