#css seletor
#봄노래로 연습해보기
import urllib
keyword='봄'
#http://music.naver.com/search/search.nhn?query="+keyword+"&target=track
f = urllib.urlopen("http://music.naver.com/search/search.nhn?query="+keyword+"&target=track")
mydata = f.read();
#모든 제목 출력하기
import lxml.html
from lxml.cssselect import CSSSelector
html = lxml.html.fromstring(mydata)
#tree=lxml.etree.parse('myhtml')
# construct a CSS Selector -> 
sel1 = CSSSelector('#content > div.section > div._tracklist_mytrack.tracklist_table._searchTrack > table > tbody > tr > td.artist > a> span')
# Apply the selector to the DOM tree.
nodes = sel(html)
#content > div.section > div._tracklist_mytrack.tracklist_table._searchTrack > table > tbody > tr:nth-child(2) > td.name > a._title.title> span
for node in nodes:
    #print lxml.html.tostring(item)
    print node.text_content()

    
_selName=CSSSelector('tr > td.name > a.title > span')
_selArtist=CSSSelector('tr >td._artist > a > span')
_selAlbum=CSSSelector('tr >td.album > a > span')
#content > div.section > div._tracklist_mytrack.tracklist_table._searchTrack > table > tbody > tr:nth-child(2) > td._artist.artist > a > span
#content > div.section > div._tracklist_mytrack.tracklist_table._searchTrack > table > tbody > tr:nth-child(2) > td.album > a > span
#content > div.section > div._tracklist_mytrack.tracklist_table._searchTrack > table > tbody > tr:nth-child(2) > td.name > a._title.title.NPI\3d a\3a track\2c r\3a 1\2c i\3a 1782765 > span
_name=_selName(nodes[0])
_artist=_selArtist(nodes[0])
_album=_selAlbum(nodes[0])

print _name[0].text_content()
print _artist[0].text_content().strip()
print _album[0].text_content()

_selName = CSSSelector('tr > td.name > a.title ')
_selArtist=CSSSelector('tr >td._artist > a ')
_selAlbum=CSSSelector('tr >td.album > a ')
#반복문을 이용하여 모든 노래를 출력한다.
#if문은 노래제목이 있는 없는 경우 제거한다 (제목 행을 제거하는 효과)
for node in nodes:
    #print lxml.html.tostring(item)
    _name=_selName(node)
    _artist=_selArtist(node)
    _album=_selAlbum(node)
    if _artist:
        print _artist[].text_content().strip(),
        print "---",
        print _name[].text_content(),
        print "---",
        print _album[].text_content()