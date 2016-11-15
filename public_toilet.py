import os
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

KEY=key['dataseoul']
TYPE='xml'
SERVICE='GeoInfoPublicToilet'
START_INDEX='1'
END_INDEX='10'
OBJECTID= '1'

url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX
url+='/'
url+=OBJECTID

import requests
_data=requests.get(url)
print _data.text

import requests
import lxml
import lxml.etree

_data = requests.get(url).text
tree=lxml.etree.fromstring(_data.encode('utf-8'))

nodes=tree.xpath('row')
for node in nodes:
    o=node.xpath('OBJECTID')
    g=node.xpath('GU_NM')
    h=node.xpath('HNR_NAM')
    m=node.xpath('MTC_AT')
    ma=node.xpath('MASTERNO')
    s=node.xpath('SLAVENO')
    n=node.xpath('NEADRES_NM')
    c=node.xpath('CREAT_DE')
    x=node.xpath('X')
    y=node.xpath('Y')
    
    print o[0].text ,g[0].text 
    print h[0].text, m[0].text
    print ma[0].text, s[0].text
    print n[0].text, c[0].text
    print x[0].text, y[0].text