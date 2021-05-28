header =[] #첫줄변수

s_data = [] 

c_list = []


ed_list = []
endprice = 0


st_list = []
startprice = 0

bfprice = 0
afprice = 0
maxprice = 0

upcounter = 0
downcounter = 0
samecounter = 0
line_counter = 0

result_list = []

days = {} #등락여부 카운트

pidays= {} #매수 매도 합산값

buyval = 1
sellval = 1

with open ('가격정보.csv','r') as costname:

    while 1:
        data = costname.readline()

        if not data: #마지막줄에서 뒤로 한칸 가서 종가 확인하는법?
            ed_list = data.split(",")
            endprice = bfprice
            break

        if line_counter==0: #첫번째 줄 헤더설정. 
            header = data.split(",")
        else:           
            if line_counter==1: #두번째 줄에서 시작가격 변수에 넣음. 
                sp_list = data.split(",")
                startprice = int(sp_list[2])
                
            c_list = data.split(",") #리스트 읽기
            day = c_list[1]
            #tot_list.append(c_list)

            if int(c_list[2])>maxprice: #기간최고가
                maxprice = int(c_list[2])

            if day not in days: #날짜별 상승여부
                days[day] = {'up':0, 'down':0, 'same':0}
                
            if day not in pidays: #날짜별 매도 매수값
                pidays[day] = {'buy':0, 'sell':0}

            pidays[day]['buy'] += int(c_list[4]) #매수매도량 요일별 기입
            pidays[day]['sell'] += int(c_list[5])

            if int(c_list[2]) > bfprice:  # 이전가격 비교해서 상승했을경우 upcounter+1
                days[day]['up'] +=1
                
            elif int(c_list[2]) < bfprice: # 이전가격 비교해서 하락했을경우 downmcounter+1
                days[day]['down'] +=1
                
            else: # 이전가격 비교해서 동일했을경우 samecounter+1
                days[day]['same'] +=1

            

            bfprice = int(c_list[2])
                

        line_counter +=1



print("시작, 종료가격, 기간최고가", startprice, endprice, maxprice)
print(days) #일자별 통계치

print(pidays) #매수매도 트렌드
