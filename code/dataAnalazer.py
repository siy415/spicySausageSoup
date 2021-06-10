"""
    코딩: 정보경
"""
from typing import Dict, List
import pandas as pd
from requests.models import parse_header_links
import readFinanceData

def dataAnalyze(corp_code, start_date=None, end_date=None): #정보경 분석 완료 데이터 return
    param = {
        "start_val"  : int,
        "end_val"    : int,
        "se_val"     : int,
        "max_val"    : int,
        "min_val"    : int,
        "mm_val"     : int,
        "stockData"  : List,
    }

    print(start_date, end_date)

    pdata = readFinanceData.DataReader(corp_code, start_date, end_date) #정보경 데이터 분석 시작
    if len(pdata) > 0:
        df2 = pd.DataFrame(pdata)
        #df2.head()
        #print(df2[:0])#헤더

        start_val = df2.iloc[0][5] #시작날짜 종가
        #print('시작일자 종가:', int(start_val))

        end_val = df2.iloc[-1][5] #마지막날짜 종가
        #print('종료일자 종가:', int(end_val))

        se_val = int(end_val)-int(start_val) #시작일, 종료일 차이
        #print('시작일자, 종료일자 차이: ', se_val)

        max_val = df2['Close'].max() #기간 내 최고가
        #print('기간 내 최고가:', int(max_val))

        min_val = df2['Close'].min() #기간 내 최저가
        #print('기간 내 최저가:', int(min_val))

        mm_val = int(max_val)-int(min_val) #정보경 기간 내 최고, 최저가 차이
        #print('기간 내 최고가, 최저가 차이:', mm_val)

        param["start_val"] = start_val
        param["end_val"]   = end_val
        param["se_val"]    = se_val
        param["max_val"]   = max_val
        param["min_val"]   = min_val
        param["mm_val"]    = mm_val

        df2['Up8']=df2.Close > df2.Close.shift() # 상승 한 경우 True
        df2['Same9'] = df2.Close == df2.Close.shift() # 동일값일 경우 True
        df2['Down10'] = df2.Close < df2.Close.shift() # 하락 한 경우 True

        print(df2)
        #df2['Days'] = df2['Date'].dt2.weekday 날짜 column 기입

        stockData = [] #정보경 리스트 선언
        lstDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] #리스트 조건

        i = 0
        for dow in lstDays: #정보경 상승하락동일 카운트\
            df3 = df2[pdata['DOW'] == dow]
            up_count = len(df3[df3['Up8'] == True]) #up count
            same_count = len(df3[df3['Same9'] == True]) #same count
            down_count = len(df3[df3['Down10'] == True]) #down count

            total_count = len(df3) #total값
            
            #정보경 상승하락동일 퍼센트계산
            up_countval = round((up_count/total_count)*100,2) # 퍼센트단위 계산
            same_countval = round((same_count/total_count)*100,2)
            down_countval = round((down_count/total_count)*100,2)

            #정보경 count 값 dict 저장
            dict = {
                'up'      : up_count,
                'down'    : down_count, 
                'same'    : same_count, 
                'total'   : total_count, 
                'upval'   : up_countval, 
                'sameval' : same_countval, 
                'downval' : down_countval
            } 
            stockData.append(dict)
            i += 1
            
        korDays = ["월요일", "화요일", "수요일", "목요일", "금요일"]
        #정보경 매수 매도 추천일자 출력.

        recommend = {}
        recommend["sell"] = []
        recommend["stay"] = []
        recommend["buy"] = []

        for i in range(len(stockData)):
            up   = stockData[i].get('upval')
            down = stockData[i].get('downval')
            same = stockData[i].get('sameval')

        #정보경 데이터 분석 시작
            if up == down or \
            up == same or \
            down == same:
                pass
            elif up == max(up, down, same):
                    recommend["sell"].append(korDays[i])
            elif same == max(up, down, same):
                    recommend["stay"].append(korDays[i])
            else:
                    recommend["buy"].append(korDays[i])

        #print('매수:', recommend["sell"])
        #print('관망:', recommend["stay"])
        #print('매도:', recommend["buy"])

        #print('각 일자별 카운트: ', stockData)

        param["stockData"] = stockData
        param["recommend"] = recommend
        
        return param

#param = dataAnalyze('005930', '2019-04-04', '2021-12-31')

# print example
#ll = param.items()
#for i in ll:
#    print(i)

""" example
    param["start_val"] : int
    param["end_val"] : int
    param["se_val"] : int
    param["max_val"] : int
    param["min_val"] : int
    param["mm_val"] : int

    stockData = param["stockData"][0-4]   ------> dict,     [0-4] = [월, 화, 수, 목, 금]
    stockData["up"] : int
    stockData["down"] : int
    stockData["same"] : int
    stockData["total"] : int
    stockData["up"] : int
    stockData["upval"] : float
    stockData["sameval"] : float
    stockData["downval"] : float

    recommand = param["recommand"]    --------> dict
    recommand["sell"][0 - len(recommand["sell"])]    
    recommand["stay"][0 - len(recommand["sell"])]    
    recommand["buy"][0 - len(recommand["sell"])]    
"""

"""
for k, v in param.items():
    if type(v) == dict or type(v) == defaultdict:
        for kk, vv in v.items():
            print(kk + ": ", + vv)
    elif type(v) == list:
        for vv in v:
            print(vv)
    else:
        print(type(v))
"""
