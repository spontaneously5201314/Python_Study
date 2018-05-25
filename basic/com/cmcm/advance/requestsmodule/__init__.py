# 使用requests模块的原因是因为该模块在python2和python3中的方法是一样的
# 而python自带的urllib模块在python2和python3中的方法是不一样的

# response.text和response.content的区别
# response.text
#     类型: str
#     解码类型: 根据HTTP头部对相应的编码做出的有根据的推测,推测文版的编码
#     如何修改编码方式: response.encoding="gbk"
# response.content
#     类型: bytes
#     解码类型: 没有指定
#     如何修改编码方式: response.content.decode("utf-8")
# 更推荐使用response.content.decode()的方式获取响应的html页面,因为如果有图片这种信息返回,最好还是二进制保存
# response的常用方法:
#     response.text
#     response.content
#     response.status_code
#     response.request_headers
#     response.headers
#
# 哪些地方会使用到post请求,爬虫也会对这两个地方发送post请求
#     登录注册
#     需要传输大文本内容的时候(post请求对数据长度没有限制)
