
import oauth2 as oauth
def getApiKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        if(row[0]!='debug'):
            row0=row[0].split('.')
            d[row0[1].upper()]=row[1].strip()
    return d
key={'CONSUMERKEY':'O66W3pL3dtMAJWRy0VYKFFIhv','CONSUMERSECRET':'GrE8hAbT39XYpt2erMIsyioNixC3A40qjIxl70BBXlrcM4yVuH','ACCESSTOKEN':'786095471613841408-7Gt0CQorSSy1i34LWtdeR6MY4PHDeUv','ACCESSTOKENSECRET':'QDCHMovCOqWqwvECcDB7yPWRNQScrpjEve2HZRu1L8siM'}

import urllib
url1 = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'seoul','count':20}
mybody=urllib.urlencode(myparam)

resp, tsearch = client.request(url1+"?"+mybody, method="GET")
tsearch_json = json.loads(tsearch)
print type(tsearch_json)
print tsearch_json.keys()
print len(tsearch_json['statuses'])