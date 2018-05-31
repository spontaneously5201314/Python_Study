# 展示不同国家电视剧平衡的平均值
from pymongo import MongoClient
import pandas as pd
import numpy as np


# 从MongoDB库中读取数据,转换为DataFrame
def load_data():
    client = MongoClient(host="127.0.0.1", port=27017)
    collection = client["duanzi"]["qiubai"]
    data_temp = collection.find()
    # print(data_temp)
    data_set = []
    for data in data_temp:
        list = {}
        list["author_name"] = data["author_name"]
        if data["author_age"] is not None:
            list["author_age"] = data["author_age"]
        else:
            break
        list["stats_vote"] = data["stats_vote"]
        list["stats_comments"] = data["stats_comments"]
        data_set.append(list)
    return pd.DataFrame(data_set)


def process_data(data_set):
    print(data_set.shape)
    print(data_set.values)
    print(data_set.info())
    print(data_set.describe())
    # print(data_set.head(3))
    # new_df = data_set.groupby("author_age")
    # print(new_df)
    # new_df = new_df["rating_value"]
    # print(new_df)


def run():
    # 1.明确问题,选择呈现数据的图形
    # 2.获取数据
    data_set = load_data()
    # 3.处理数据
    process_data(data_set)
    # 4.画图


if __name__ == '__main__':
    run()
