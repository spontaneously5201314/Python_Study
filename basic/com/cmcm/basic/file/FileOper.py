f = open('/opt/pycharm/workspace/Python_Study/basic/com/cmcm/HelloWorld/Unicode.py', 'r')
# print(f.read())
#移动指针到特定位置
# f.seek(0)
# print(f.read())
#close不是必须的，但是建议有
# f.close()
# f.seek(0)
#readlines按行读取到一个列表中
# l = f.readlines()
# print(l)
# f.write("hon")
# f.writelines(['tom'])
# f.flush()


#好一点的写法，这样就不用在每次文件操作之后要显示写close了
with open('/opt/pycharm/workspace/Python_Study/basic/com/cmcm/HelloWorld/Unicode.py','r', encoding='utf8') as f:
    for line in f:
        print(line)