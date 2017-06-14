# People-Movement-Map
本项目目的是通过城市的交通态势来展示城市人口的转移情况。  
城市中人们出行的高峰会使道路出现拥堵，道路的方向既是人们需要去的方向，因此通过城市交通数据可以在一定程度上分析人口转移情况。  
通过'data.py'从高德地图的交通态势数据。  
'xmlparse.py'分析数据。  
'map.py'下载一份可以使用的地图图片。  
'location.py'将点的坐标转化成图片上的像素位置。 
'arrow.py'绘制箭头，分四个方向。  
'image.py'绘制成图，完成展示。  


data.py can download the data of the trafficinfo rhight now, the type is XML. 
xmlparse.py can parse the xml data file.  
map.py download a map that provided by amap.  
location.py this file make a tranlation of pixel location and geo coordinates.  
arrow.py can make a arrow with the data.  
image.py is the final draw the arrow on the map.  
