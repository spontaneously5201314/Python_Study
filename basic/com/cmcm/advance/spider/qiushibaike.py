# 抓取糗事百科热门
import requests
from lxml import etree
from pymongo import MongoClient

client = MongoClient("127.0.0.1", 27017)
collection = client["duanzi"]["qiubai"]  # 前面取的是数据库,后面取的是集合


def generate_url_list(pages):
    url_list = []
    url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
    for i in range(1, pages):
        url_list.append(url_temp.format(i))
    return url_list


def send_request(url):
    headers = {
        # 一定要注意这里的User-Agent,如果换成是手机的代理,可能返回的结果中就没有我们需要的标签,就不能解析成功,就会返回没有数据
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    }
    response = requests.get(url, headers=headers, timeout=5)
    html_resp = response.content.decode()
    return etree.HTML(html_resp)  # 使用etree处理,得到element对象,能够直接使用xpath方法


def collect_content(html_resp):
    div_list = html_resp.xpath("//div[@id='content-left']/div")
    contents = []
    for div in div_list:
        item = {}
        # 获取用户的头像图片
        item["author_img"] = div.xpath("./div[@class='author clearfix']//img/@src")
        if len(item["author_img"]) > 0:
            item["author_img"] = "https:" + item["author_img"][0]
        else:
            item["author_img"] = None
        # 获取用户的用户名
        item["author_name"] = div.xpath("./div[@class='author clearfix']//h2/text()")
        if len(item["author_name"]) > 0:
            item["author_name"] = item["author_name"][0].strip()
        else:
            item["author_name"] = None
        # 获取性别
        item["author_gender"] = div.xpath("./div[@class='author clearfix']//div/@class")
        if len(item["author_gender"]) > 0:
            item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon", "")
        else:
            item["author_gender"] = None
        # 获取年龄
        item["author_age"] = div.xpath("./div[@class='author clearfix']//div/text()")
        if len(item["author_age"]) > 0:
            item["author_age"] = item["author_age"][0]
        else:
            item["author_age"] = None
        # 取用户发表的内容
        item["content"] = div.xpath(".//div[@class='content']/span/text()")
        item["content"] = [i.strip() for i in item["content"]]  # 列表推倒式
        # 获取该条内容的点赞数量
        item["stats_vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")
        if len(item["stats_vote"]) > 0:
            item["stats_vote"] = item["stats_vote"][0]
        else:
            item["stats_vote"] = None
        # 提取评论数量
        item["stats_comments"] = div.xpath(".//span[@class='stats-comments']//i/text()")
        if len(item["stats_comments"]) > 0:
            item["stats_comments"] = item["stats_comments"][0]
        else:
            item["stats_comments"] = None
        # 获取正文中的图片
        item["content_img"] = div.xpath("./div[@class='thumb']//img/@src")
        if len(item["content_img"]) > 0:
            item["content_img"] = "https:" + item["content_img"][0]
        else:
            item["content_img"] = None
        contents.append(item)
    return contents


def save_pig(url):
    # https://pic.qiushibaike.com/system/pictures/11138/111388717/medium/app111388717.jpg
    # 获得图片的名字
    # print(type(url))
    name_first = str.rindex(url, "/", 0, len(url))
    name_last = str.rindex(url, ".", 0, len(url))
    pig_name = url[name_first:name_last]
    # 获取图片的格式
    suffix = url[(name_last + 1):len(url)]
    response = requests.get(url)

    pig = open("./qiubaipig/{}.{}".format(pig_name, suffix), "wb")
    pig.write(response.content)
    pig.flush()
    pig.close()


def save_contents(contents):
    for content in contents:
        collection.insert(content)
        # 5.保存下每个内容里面的图片,假设有的话
        # if content["content_img"] is not None:
        #     save_pig(content["content_img"])


def run():
    pages = 14
    # 1.发现url的规律,构造一堆url出来
    url_list = generate_url_list(pages)
    for url in url_list:
        # 2.遍历url_list,发送请求,获取响应数据
        response = send_request(url)
        # 3.提取数据
        contents = collect_content(response)
        # 4.保存数据
        save_contents(contents)


if __name__ == '__main__':
    run()
