# for in循环
for i in range(100):
    print("现在进行第{}次循环".format(i))
    if i % 2 == 0:
        continue
    print(i.bit_length())  # bit_length返回的是一个数字的二进制位数
# pep8规范，是Python的规范
