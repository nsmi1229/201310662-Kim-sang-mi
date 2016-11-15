
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

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX=str(1)
END_INDEX=str(10)
LINE_NUM=str(2)

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)
print params[31:]

import urlparse
_url='http://openAPI.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)

import requests
data=requests.get(url).text
print data

type(data)

import re
p=re.compile('<STATION_NM>(.+?)</STATION_NM>')
res=p.findall(data)
for item in res:
    print item
    
import xml.etree.ElementTree as ET
tree=ET.fromstring(data.encode('utf-8'))
In [110]:

stds=tree.findall('row')
for elements in stds:
    for elm in elements:
        print elm.text
        
import lxml
import lxml.etree
import StringIO

tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATION_NM')
for node in nodes:
    print node.text