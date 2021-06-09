from typing import List
# import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd
import readFinanceData

# 삼성전자(005930) 전체 (1996-11-05 ~ 현재)
df = readFinanceData.DataReader('005930', '2005-05-01', 'now')
cnt = 0
blShow: List

blShow = []

for col in df.head():
    if col == 'Close':
        blShow.append(True)
    else:
        blShow.append(False)

def getData():
    for ma in ma_ls:
        if ma < len(df):
            maClose = df['Close'].rolling(window=ma, min_periods=1).mean()
            df['MA' + str(ma)] = maClose
            blShow.append(True)

    df.iloc[:, [4]].plot(kind='bar', rot=0)
    print(df['Volume'])
    df.iloc[:, blShow].plot()

    return df, blShow