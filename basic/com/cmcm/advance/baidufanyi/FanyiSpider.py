import requests
import json

url = "http://fanyi.baidu.com/v2transapi"


def trans_cn_to_en(cn):
    data = {
        "from": "zh",
        "to": "en",
        "query": cn,
        "transtype": "translang",
        "simple_means_flag": 3,
        "sign": "966972.664077",
        "token": "b6fbe776a40072e8d5607dd30bcc811a"
    }
    headers = {
        "User-Agent": "Mozilla / 5.0(X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 57.0.2987.133 Safari / 537.36"
    }
    response = requests.post(url, data=data, headers=headers)
    en = response.content.decode("utf-8")
    print(response.content)
    print(response.content.decode("utf-8"))
    print("中文{}的英文翻译是{}".format(cn, en))


trans_cn_to_en("姓名")

#
# cns = ["名称"]
#
# for cn in cns:
#     trans_cn_to_en(cn)
