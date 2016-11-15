
def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d

import os
keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=getKey(keyPath)

import requests
import re
busstopurl='http://openAPI.seoul.go.kr:8088/sample/xml/CardBusStatisticsService/1/5/201510/7016'
data=requests.get(busstopurl).text
print data
p=re.compile('<BUS_STA_NM>(.+?)</BUS_STA_NM>')
res=p.findall(data)
for item in res:
print item

buspassengers='http://openAPI.seoul.go.kr:8088/sample/xml/CardBusStatisticsService/1/5/201510/7016/'
data=requests.get(busstopurl).text
print data
p=re.compile('<RIDE_PASGR_NUM>(.+?)</RIDE_PASGR_NUM>')
res=p.findall(data)
for item in res:
    print item
    

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='CardBusStatisticsService'
START_INDEX=str(1)
END_INDEX=str(5)
USE_MON=str(201512)
BUS_ROUTE_NO=str(7016)

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,USE_MON,BUS_ROUTE_NO)
print params[31:]

import urlparse
_url='http://openapi.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)

import requests
data=requests.get(url).text
print data