from typing import List
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd

ma_ls = [5, 20, 60, 120]

# 삼성전자(005930) 전체 (1996-11-05 ~ 현재)
df = fdr.DataReader('005930', '2021-05-01', 'now')
print(len(df))
cnt = 0
blShow: List

blShow = []
for col in df.head():
    if col == 'Close':
        blShow.append(True)
    else:
        blShow.append(False)


for ma in ma_ls:
    if ma < len(df):
        maClose = df['Close'].rolling(window=ma, min_periods=1).mean()
        df['MA' + str(ma)] = maClose
        blShow.append(True)

df.iloc[:, [4]].plot(kind='bar', rot=0)
print(df['Volume'])
df.iloc[:, blShow].plot()

plt.show()