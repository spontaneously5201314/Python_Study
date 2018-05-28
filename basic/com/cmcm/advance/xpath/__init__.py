from lxml import etree
import requests


# 好一点的分组方式是,根据某个标签分组,对分组中的每一条数据继续写xpath,这样就不会出现因为其中一条数据
# 的某个属性为空,就出现了分组错乱的问题


def get_html(url):
    response = requests.get(url)
    return response


def convert_html(html_str):
    html = etree.HTML(html_str)
    print(etree.tostring(html).decode())


if __name__ == '__main__':
    result = get_html("https://www.baidu.com")
    convert_html(result)
