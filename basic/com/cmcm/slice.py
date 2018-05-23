L = ['Adam', 'Lisa', 'Bart', 'Paul']

# print(L[-2:])
#
# print('ABCDEFG'[:3])

for index, name in enumerate(L):
    print(index, '--', name)


print(enumerate(L))

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }

# print(d.values())

# for value in d.__iter__():
#     print(value)

print(d.items())

for key, value in d.items():
    print(key, ".....", value)