#regex
import urllib
response = urllib.urlopen('http://python.org/')
_html = response.read()
print response.info()
print len(_html)
import re
p=re.compile('href="(http://.*?)"')
res=p.findall(_html)
for item in res:
    print item
    import re
p=re.compile('<h1>(.*?)</h1>')
h1tags=p.findall(_html)
for i in h1tags:
    print i
    import re
p=re.compile('<p>(.*?)</p>')
ptags=p.findall(_html)