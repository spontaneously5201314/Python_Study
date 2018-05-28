# 请使用 chrome 浏览器工具查找 http://tv.cctv.com/2014/07/07/VIDA1404730290373811.shtml 湄公河第一集视频的URL
# 1、使用 chrome 浏览器打开第一集视频，并使用 chrome 工具查找 guid 的值
# 2、对 URL http://vdn.apps.cntv.cn/api/getIpadVideoInfo.do?pid= 与 查
# 3、找的 guid 的值进行拼接，得到视频 URL 信息链接
# 4、使用 requests 库发送请求获取视频信息 response
# 5、对 response 进行字符处理得到满足 json 格式的数据
# 6、请使用 json 模块吧得到 json 格式数据保存到当前文件夹下面的 video_info.txt 文件中
from lxml import etree
import requests
import json


def get_video(url):
    response = requests.get(url)
    # print(type(response.content.decode("utf-8")))
    str = response.content.decode("utf-8");
    first_index = str.find("'", 0, len(str))
    last_index = str.rfind("'", 0, len(str))
    need_str = str[first_index + 1:last_index]
    result = json.loads(need_str)
    f = open("video_info.txt", "w")
    f.write(json.dumps(result))
    f.flush()
    f.close()


def get_all_video():
    response = requests.get("http://tv.cctv.com/2014/07/07/VIDA1404730290373811.shtml")
    response.encoding = "utf-8"
    selector = etree.HTML(response.text)
    xpath_reg = "//div[@class='text_mod']/h3/text()"    # 提取湄公河的标题的xpath规则
    results = selector.xpath(xpath_reg)     # 使用xpath表达式进行数据提取,反馈结果是一个列表
    title = results[0]      # 列表中以后一个数据所以直接提取得到数据
    print(title)



if __name__ == '__main__':
    # &tai=ipad&from=html5&tsp=1527405728&vn=2049&vc=6206F5EBFAEF325B5C97132A2B2230AA&uid=80F083DB849C4A25D28BFE24CE26994C&wlan=
    url = "http://vdn.apps.cntv.cn/api/getIpadVideoInfo.do?pid=59381a0e55404cf5b101f7d3bcad2da8"
    get_video(url)
