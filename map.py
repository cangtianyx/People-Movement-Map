# -*- coding=utf-8 -*- 

import urllib
import urllib2

url = 'http://restapi.amap.com/v3/staticmap?location=87.603915,43.819378&zoom=12&size=1024*1024&key=4e1d6de93e6ef6ec5ca542dfa0be0668'
req = urllib2.Request(url)
page = urllib2.urlopen(req)
html = page.read()

map = open('map.png','wb')
map.write(html)
map.close()


87.629921,43.859260
87.577908,43.779496
87.603915,43.819378