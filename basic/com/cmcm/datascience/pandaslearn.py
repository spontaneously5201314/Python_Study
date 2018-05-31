import pandas as pd
import numpy as np
import string

# np.random.randint能够帮助我们随机生成一定范围内的一定形状的数组
df = pd.DataFrame(np.random.randint(0, 100, (3, 4)), index=list(string.ascii_uppercase[:3]),
                  columns=list(string.ascii_uppercase[:4]))
# 手动给某个位置上赋值为Nan
df.loc["A", "A"] = np.nan
df.loc["A", "D"] = 0
print(df)

# isnull判断哪些是null
# print(pd.isnull(df))

# 选择W列中部位NAN的那几行
# new_df = df[pd.notnull(df["A"])]
# print(new_df)

# 填充数据
# df.fillna(df.mean(), inplace=True)
# print(df)

# 分组聚合
grouped = df.groupby(by="D")
type(grouped)
for i in grouped:
    print(grouped)