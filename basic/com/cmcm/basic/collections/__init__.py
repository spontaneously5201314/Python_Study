numbers = [1, 2, 3, 45, 6]
print(numbers)


L = ['Adam', 'Lisa', 'Bart']
# print(L[3])
# print(L[-2])
L.append('hongfei')
L.insert(1, 'zhangsan')
print(L)

for name in L:
    print(name)

L.pop()
print(L)

L.pop(1)
print(L)

T = (1,)
print(T)