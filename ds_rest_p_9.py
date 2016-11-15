
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
weatherurl='http://openAPI.seoul.go.kr:8088/sample/xml/RealtimeWeatherStation/1/5/'
data=requests.get(weatherurl).text
print data
p=re.compile('<SAWS_TA_AVG>(.+?)</SAWS_TA_AVG>')
res=p.findall(data)
for item in res:
    print item
KEY=str(key['dataseoul'])
TYPE='json'
SERVICE='RealtimeWeatherStation'
START_INDEX=str(1)
END_INDEX=str(5)
STN_NM=u'중구'

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,STN_NM)
print params[31:]

import urlparse
_url='http://openapi.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)


import requests
data=requests.get(url).text
print data