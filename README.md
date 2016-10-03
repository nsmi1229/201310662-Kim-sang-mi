# 201310662-Kim-sang-mi
.
import urllib
response = urllib.urlopen('http://python.org/')
_html = response.read()
print response.info()
print len(_html)
