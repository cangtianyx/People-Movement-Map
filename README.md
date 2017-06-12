# People-Movement-Map
These files can make a image of map that shows people's movement in some movement in a day. All of the data is get in a map app called "Gao De Di Tu" and the address is 'http://lbs.amap.com/api/webservice/guide/api/trafficstatus'.


data.py can download the data of the trafficinfo rhight now, the type is XML.
xmlparse.py can parse the xml data file.
map.py download a map that provided by amap.
location.py this file make a tranlation of pixel location and geo coordinates.
arrow.py can make a arrow with the data.
image.py is the final draw the arrow on the map.
