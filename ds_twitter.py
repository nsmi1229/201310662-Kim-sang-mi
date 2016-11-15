
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

import oauth2 as oauth
import json
consumer=oauth.Consumer(key=key['CONSUMERKEY'],secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])
client=oauth.Client(consumer,token)
import urllib
url = "https://api.twitter.com/1.1/statuses/update.json"
mybody=urllib.urlencode({'status': 'Hello 21 161113'})
response,content=client.request(url,method='POST',body=mybody)
#print content

print response