pdata = df
#print(type(pdata))

df2 = pd.DataFrame(pdata)
df2.head()
print(df2[:0])#헤더

start_val = df2.iloc[0][5] #시작날짜 종가
print('시작일자 종가:', int(start_val))

end_val = df2.iloc[-1][5] #마지막날짜 종가
print('종료일자 종가:', int(end_val))

se_val = int(end_val)-int(start_val) #시작일, 종료일 차이
print('시작일자, 종료일자 차이: ', se_val)

max_val = df2['Close'].max() #기간 내 최고가
print('기간 내 최고가:', int(max_val))

min_val = df2['Close'].min() #기간 내 최저가
print('기간 내 최저가:', int(min_val))

mm_val = int(max_val)-int(min_val) #기간 내 최고, 최저가 차이
print('기간 내 최고가, 최저가 차이:', mm_val)



df2['Up8']=df2.Close > df2.Close.shift() # 상승 한 경우 True
df2['Same9'] = df2.Close == df2.Close.shift() # 동일값일 경우 True
df2['Down10'] = df2.Close < df2.Close.shift() # 하락 한 경우 True

print(df2)
#df2['Days'] = df2['Date'].dt2.weekday 날짜 column 기입

days = {} #등락여부 카운트

items = {} #딕셔너리 선언
l = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] #리스트 조건

for dow in l: #상승하락동일 카운트
    df3 = df2[df['DOW'] == dow]
    up_count = len(df3[df3['Up8'] == True]) #up count
    same_count = len(df3[df3['Same9'] == True]) #same count
    down_count = len(df3[df3['Down10'] == True]) #down count

    total_count = len(df3) #total값
    
    #상승하락동일 퍼센트계산
    up_countval = round((up_count/total_count)*100,2) # 퍼센트단위 계산
    same_countval = round((same_count/total_count)*100,2)
    down_countval = round((down_count/total_count)*100,2)

    items[dow] = {'up': up_count, 'down': down_count, 'same': same_count, 'total': total_count, 
    'upval': up_countval, 'sameval': same_countval, 'downval': down_countval} #count 값 dict 저장

print('각 일자별 카운트: ', items)
