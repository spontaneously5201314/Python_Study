import requests as rq

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
}

result = rq.get("http://www.baidu.com", headers=headers)
# print(type(result))
print(result.headers)
# print(result.text)
# print(result.content)
print(result.content.decode("utf-8"))
