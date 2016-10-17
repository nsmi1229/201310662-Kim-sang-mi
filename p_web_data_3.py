#csssector
import lxml.html
from lxml.cssselect import CSSSelector
import requests
r = requests.get('http://python.org/')

html = lxml.html.fromstring(r.text)
sel=CSSSelector('a[href]')
results = sel(html)
print len(results)
for item in results:
    print item.get('href'), item.text