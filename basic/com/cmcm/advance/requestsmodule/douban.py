# 主要用来爬豆瓣电影的数据
import requests
import json

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Host": "movie.douban.com",
    "Referer": "https://movie.douban.com/tag/",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
}


def get_url_list():
    url_list = [
        "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0"
    ]
    return url_list


def send_request(url):
    response = requests.get(url, headers=headers)
    return response


def parse_response(data):
    return json.loads(data, encoding="utf-8")


def save_data(movies):
    print(movies)
    for data in movies["data"]:
        acters = data["casts"]
        for cast in acters:
            print("casts:{}".format(cast))
        print("directors:{}".format(data["directors"]))
        print("title:{}".format(data["title"]))
        print("url:{}".format(data["url"]))


# 主要方法
def run():
    # 1.获取url地址列表
    url_list = get_url_list()
    for url in url_list:
        # 2.针对url地址列表中的每个url发起请求
        response = send_request(url)
        # 3.记录下访问返回的数据,并进行数据处理
        data = parse_response(response.content.decode("utf-8"))
        # 4.保存数据
        save_data(data)


if __name__ == '__main__':
    run()
