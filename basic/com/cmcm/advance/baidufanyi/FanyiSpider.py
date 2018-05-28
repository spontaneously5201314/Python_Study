import requests
import json
import sys

url = "http://fanyi.baidu.com/v2transapi"

# 获取我们要执行的py文件后面的字符串
tran_str = sys.argv[1]


def trans_cn_to_en():
    data = {
        "from": "zh",
        "to": "en",
        "query": tran_str,
        "transtype": "translang",
        "simple_means_flag": "3",
        "sign": "966972.664077",
        "token": "d8d269698955417db04b0399cbbe3fb9"
    }
    headers = {
        "User-Agent": "Mozilla / 5.0(X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 57.0.2987.133 Safari / 537.36"
    }
    response = requests.post(url, headers=headers, data=data)
    # print(response.content)
    en = response.content.decode("utf-8")
    # print(response.content.decode("utf-8"))
    print(en)
    # result_dict = json.loads(en)
    # print(result_dict)
    # result = result_dict["trans_result"]["data"][0]["dst"]
    # print("中文{}的英文翻译是{}".format(cn, result))


trans_cn_to_en()
#
# cns = ["名称"]
#
# for cn in cns:
#     trans_cn_to_en(cn)
