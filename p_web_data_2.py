#xpath
import urllib
response = urllib.urlopen('http://python.org/')
_html = response.read()
print response.info()
from lxml import etree
_htmlTree = etree.HTML(_html)
result = etree.tostring(_htmlTree, pretty_print=True, method="html")
nodes = _htmlTree.xpath('//*[@href]')
for node in nodes:
    print node.attrib