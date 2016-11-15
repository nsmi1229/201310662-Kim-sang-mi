import os
import urllib
import urlparse

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    lines=f.readlines()
    for line in lines:
        row=line.split('=')
        row0=row[0]
        d[row0] =row[1].strip()
    return d

keyPath=os.path.join(os.getcwd(),'src','key.properties')

key=getKey(keyPath)

SERVICE='KorService'
OPERATION_NAME='searchKeyword'
param1=SERVICE+'/'+OPERATION_NAME

d=dict()
d['areaCode']='1'
param2=urllib.urlencode(d)
params=param1+'?'+'serviceKey='+key['gokr']+'&'+param2

url='http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchKeyword'
myurl=urlparse.urljoin(url,params)

import requests
data=requests.get(myurl).text
print data

import re
f=open('my.txt','w')
p=re.compile('<NORMAL_CODE>(.+?)</MNORMAL_CODE>')
res=p.findall(data)   
for item in res:
    print item
    f.write(item)
    f.write('\n')
f.close()