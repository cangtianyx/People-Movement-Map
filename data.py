# -*- coding=utf-8 -*-
#this app use amap API to get all the residence community in shuimogou area of Urumqi.
#thanks to amap company. please visit http://ditu.amap.com/ to get more information



import urllib
import urllib2
import time
import winsound

#this url is incould chinese:
#url_amap = 'http://restapi.amap.com/v3/traffic/status/road?key=4e1d6de93e6ef6ec5ca542dfa0be0668&name=%E7%BA%A2%E5%B1%B1%E8%B7%AF&adcode=650100&output=XML' 


# my amap key = 4e1d6de93e6ef6ec5ca542dfa0be0668 . The key is onle owned by Li DongYue , if you need to use it ,pls send a mail to 705078495@qq.com to get the permission.

def function():
	url_amap = 'http://restapi.amap.com/v3/traffic/status/rectangle?rectangle=87.629921,43.85926;87.577908,43.779496&output=XML&extensions=all&key="YOUR KEY"'
	req = urllib2.Request(url_amap)
	page = urllib2.urlopen(req)
	html = page.read()
	a = time.strftime('%m-%d %H-%M', time.localtime())
	print a
	num1 = open('%s.xml' % a,'w+')
	num1.write(html)
	num1.close()

while True:
	function()
	time.sleep(1800)      # every half a hour get the data one time
	winsound.Beep(1000,1000)

