import re
import requests
import pandas as pd
from pandas import to_datetime
from io import StringIO
from datetime import datetime



def _validate_dates(start_date, end_date):  # readFinanceData by Jang Dongchan
    start_date = to_datetime(start_date)
    end_date = to_datetime(end_date)

    if start_date is None:
        start_date = datetime(1970, 1, 1)
    if end_date is None:
        end_date = datetime.today()
    return start_date, end_date


class WebDataReader:  # readFinanceData by Jang Dongchan

    def __init__(self, corp_code, start_date=None, end_date=None):
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
        df = pd.DataFrame(pd.read_csv(StringIO(data), delimiter='|', header=None, dtype={0:str}))
        df.columns  = ['Date', 'Open', 'High', 'Low', 'Close','Volume']
        df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
        # df.set_index('Date', inplace=True)
        df = df.query('Date>=%r and Date<=%r' % (self.start_date, self.end_date))
        df = df.reset_index(drop=True)
        df.insert(1,'DOW', df['Date'].dt.day_name())

        df.sort_index(inplace=True)
        df['Change'] = df['Close'].pct_change()

        return df


def DataReader(corp_code, start_date=None, end_date=None):  # readFinanceData by Jang Dongchan
    start_date, end_date = _validate_dates(start_date, end_date)

    if corp_code[:5].isdigit():
        return WebDataReader(corp_code, start_date, end_date).read()
