
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

from pymongo import MongoClient
_mclient = MongoClient()
_db=_mclient.ds_twitter
_table=_db.home_timeline

from pymongo import MongoClient
_mclient=MongoClient()
_mclient['ds_twitter']

_db=_mclient.ds_twitter
_col=_db.home_timeline
url = "https://api.twitter.com/1.1/statuses/update.json"
response,content=client.request(url)
home_timeline=json.loads(content)
len(home_timeline)
home_timeline[0]['text']
print home_timeline