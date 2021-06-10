"""
    Coding By Shim Inyong
"""
from os import path
from inspect import currentframe, getframeinfo
import requests
import zipfile, io
import json as js
import xml.etree.cElementTree as etree
import datetime as dt

corpCode = {}

baseUrl = "https://opendart.fss.or.kr/api/"

# 함수 이름에 따른 api 호출
urls = {
    "getCorpCode" : "corpCode.xml?",
    "getCompany" : "company.json?",
    "getEmployees" : "empSttus.json?",
    "getStockData" : "alotMatter.json?",
    "getCompanyFin": "fnlttSinglAcnt.json?"
}

baseData = {
    "crtfc_key" : "c32cb4b63e38456c5924c2aa0675834656df6943",
}


def getCorpCode():
    global corpCode
    # 현재 실행중인 함수 명 저장
    curFunc = getframeinfo(currentframe()).function
    url = baseUrl + urls[curFunc]
    #print(url)
    data = baseData

    # requests 형식이 post일 경우 data로 넘기는데, get은 params로 넘기는 듯    
    r = requests.get(url, params=data)
    #print(r)

    # request를 통해 받은 데이터(zip, 압축파일)를 zipFile data type으로 저장
    z = zipfile.ZipFile(io.BytesIO(r.content))
    #print(z)
    z.extractall("./data")

    xml = "./data/CORPCODE.xml"

    """  Beatutiful soup를 이용한 파싱, 느림
        read_xml = open(xml, "r", encoding="utf-8").read()
        #print(read_xml)

        tag = SoupStrainer("list")

        #lxml은 그냥 xml 파일을 처리하기위한 파이썬 패키지로, bs에서 xml 내의 Tag를 쉽게 찾을 수 있도록 해줌
        # soup엔 xml의 전체 내용이 들어있음
        # soup = BeautifulSoup(read_xml, features='lxml', parse_only=tag)

        #items = soup.find_all("list")
        #for item in items:
        #    tmpCode = item.find("stock_code").text
        #    if tmpCode == str(stockCode):
        #        res = item.find("corp_code").text
    """

    context = iter(etree.iterparse(xml, events = ('start', 'end')))
    event, root = next(context)

    for event, elem in context:
        if event == 'end' and elem.tag == "list":
            corpCode[elem[2].text] = elem[0].text

    #print(corpCode)


def getCompNum(stockCode: str):
    global corpCode
    res: str

    #if not path.isdir("./data"):
    if len(corpCode) == 0 :
        getCorpCode()

    if stockCode in corpCode:
        res = corpCode[stockCode]
    else:
        res = "000000"

    return res


def getCompany(compNum: str):
    dict = {
        "corp_code" : compNum,
    }

    # 현재 실행중인 함수 명 저장
    curFunc = getframeinfo(currentframe()).function
    url = baseUrl + urls[curFunc]

    # dict간에 합쳐줌, 필요한 dict를 합쳐서 data로 한번에 넘기기위해 사용
    data = baseData
    data.update(dict)

    r = requests.get(url, params=data)
    j = js.load(io.BytesIO(r.content))
    return j


# 연도에 대한 기본값은 현재 년도(4자리)
''' 보고서 코드
    1분기 : 11013
    반기  : 11012
    3분기 : 11014
    사업  : 11011
'''
def getEmployees(compNum, year=str(dt.datetime.now().year - 1), report="11011"):
    # https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS002&apiId=2019011
    # 직원현황에 대한 파싱 예시
    dict = {
        "corp_code" : compNum,
        "bsns_year" : year,
        "reprt_code" : report,
    }

    # 현재 실행중인 함수 명 저장
    curFunc = getframeinfo(currentframe()).function
    return apiCall(dict, curFunc)


def getStockData(compNum, year=str(dt.datetime.now().year - 1), report="11011"):
    dict = {
        "corp_code" : compNum,
        "bsns_year" : year,
        "reprt_code" : report,
    }
    
    curFunc = getframeinfo(currentframe()).function
    return apiCall(dict, curFunc)


def getCompanyFin(compNum, year=str(dt.datetime.now().year - 1), report="11011"):
    dict = {
        "corp_code" : compNum,
        "bsns_year" : year,
        "reprt_code" : report,
    }
    
    curFunc = getframeinfo(currentframe()).function
    return apiCall(dict, curFunc)


def apiCall(param, func):
    url = baseUrl + urls[func]

    # dict간에 합쳐줌, 필요한 dict를 합쳐서 data로 한번에 넘기기위해 사용
    data = baseData
    data.update(param)

    r = requests.get(url, params=data)
    #print(r)
    # json 파일을 불러와서 dictionary 형태로 저장
    j = js.load(io.BytesIO(r.content))
    return j


# compNum = getCompNum("005930")
        
# print(j["list"][len(j["list"])-2])