# print(range(1, 20, 2))

# list = range(1, 20, 2)
# print(list)
import sys

# [x * x for x in range(1, 10)]
scores = [10, 20]
print("===排序===")
print(scores.sort())

print("===取值===")
print(scores[1])
print(scores[::1])
print(scores[::-1])
print("===复制===")
print([3] * 4)

names = ["1"]
# 以下两个都是数组的扩展方法
print("===拼接===")
print(names + scores)
scores = ["2"]
help(names.extend)
print(names.extend(scores))
print("===长度===")
print(len(scores))
print("===range===")
x = list(range(1, 11))
print(x)
# x.sort()

print(sys.path)
print("===查看目录===")
print(dir(sys))
print("===查看方法帮助===")
help(str.find)
