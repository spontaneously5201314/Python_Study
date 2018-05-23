import socket

# print(dir(socket))

# help(socket.socket)

# print(type(socket.socket))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.baidu.com', 80))
s.send(b'GET / HTTP/1.1\r\n\r\n')
rt = s.recv(1024)
print(rt.decode('utf-8'))
s.close()