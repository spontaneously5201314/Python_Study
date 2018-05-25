import requests

response = requests.get("https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/global/img/icons_5859e57.png")
file = open("baidu.png", "wb")  # wb是只使用二进制写入数据到本地文件
file.write(response.content)
file.close()