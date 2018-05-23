# 学习一下Python中的条件判断和循环
age = input("请输入年龄：")
age = int(age)
if 18 > age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

N = 10
x = 0
while x < N:
    print(x)
    x = x + 1
