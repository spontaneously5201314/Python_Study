s = set(['A', 'C', 'B', 'C'])
s1 = {'A', 'C', 'B'}
print(s)
print(s1)
print('D' in s)
s.remove('C')
print(s)
s.add('D')
print(s)