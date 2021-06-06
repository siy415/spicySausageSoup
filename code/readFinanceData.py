import re
import requests
import pandas as pd
from pandas import to_datetime
from io import StringIO
from datetime import datetime
import FinanceDataReader as fdr



def _validate_dates(start_date, end_date):
    start_date = to_datetime(start_date)
    end_date = to_datetime(end_date)

    if start_date is None:
        start_date = datetime(1970, 1, 1)
    if end_date is None:
        end_date = datetime.today()
    return start_date, end_date


class WebDataReader:

    def __init__(self, corp_code, start_date=None, end_date=None, exchange=None, data_source=None):
        self.corp_code = corp_code
        start_date, end_date = _validate_dates(start_date, end_date)
        self.start_date = start_date
        self.end_date = end_date

    def read(self):
        url = 'https://fchart.stock.naver.com/sise.nhn?timeframe=day&count=6000&requestType=0&symbol='
        r = requests.get(url + self.corp_code)

        data_list = re.findall('<item data=\"(.*?)\" />', r.text, re.DOTALL)
        if len(data_list) == 0:
            return pd.DataFrame()
        data = '\n'.join(data_list)
        df = pd.read_csv(StringIO(data), delimiter='|', header=None, dtype={0:str})
        df.columns  = ['Date', 'Open', 'High', 'Low', 'Close','Volume']
        df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
        df.set_index('Date', inplace=True)
        df.sort_index(inplace=True)
        df['Change'] = df['Close'].pct_change()

        return df.query('index>=%r and index<=%r' % (self.start_date, self.end_date))


def DataReader(corp_code, start_date=None, end_date=None, exchange=None, data_source=None):

    start_date, end_date = _validate_dates(start_date, end_date)

    if (corp_code[:5].isdigit() and exchange==None) or \
       (corp_code[:5].isdigit() and exchange and exchange.upper() in ['KRX', '한국거래소']):
        return WebDataReader(corp_code, start_date, end_date, exchange, data_source).read()



# 삼성전자(005930) 전체 (1996-11-05 ~ 현재)
df = DataReader('005930', '2016-04-04', '2021-12-31')
df = df.reset_index().rename(columns={"index": "id"})
#df['day-of-week'] = df['Date'].dt.day_name()
df.insert(1,'day-of-week', df['Date'].dt.day_name())
print(df)
