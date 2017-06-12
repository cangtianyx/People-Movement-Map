# -*- coding=utf-8 -*-
from PIL import Image,ImageDraw
import arrow
import location
import xmlparse


# example
open_image = Image.open('map1.png')              # open 
map_draw = ImageDraw.Draw(open_image)            # make object

for road_num in range(120):
    xmlparse.filename = '06-08 22-05.xml'
    pixel_location = location.xy_location(xmlparse.location_data()[road_num])
    direction = xmlparse.road_direction()[road_num]
    arrow_colors =  xmlparse.road_status()[road_num]
    if arrow_colors == 3 :   # 3 means block
        RGB = (255,0,0)   # red
    elif arrow_colors == 2: # 2 means slow
        RGB = (255,165,0)  # orange
    else :
        RGB = (0,255,0)
    size = 15
    if arrow_colors == 3 :
        size = 25
    elif arrow_colors == 2:
        size = 20
    arrow_location = arrow.arrow(pixel_location,size,direction)          # input the location of pixel (x,y)
    map_draw.point(arrow_location,RGB)         # choice RGB,the initial picture is not the RGB.
del map_draw                                    # the example  of ImageDraw document have this 'del' step, but not know why.
open_image.save('map/map.png','png')                # save 


#depend on my data , I run it to make a lots of images.
'''
hours = 13
minites = '05'
imagename = 1   
while True:
    open_image = Image.open('map1.png')              # open 
    map_draw = ImageDraw.Draw(open_image)            # make object
    for road_num in range(120):
        xmlparse.filename = '06-08 %d-%s.xml' % (hours, minites)
        pixel_location = location.xy_location(xmlparse.location_data()[road_num])
        direction = xmlparse.road_direction()[road_num]
        arrow_colors =  xmlparse.road_status()[road_num]
        if arrow_colors == 3 :   # 3 means block
            RGB = (255,0,0)   # red
        elif arrow_colors == 2: # 2 means slow
            RGB = (255,165,0)  # orange
        else :
            RGB = (0,255,0)
        size = 15
        if arrow_colors == 3 :
            size = 25
        elif arrow_colors == 2:
            size = 20
        arrow_location = arrow.arrow(pixel_location,size,direction)          # input the location of pixel (x,y)
        map_draw.point(arrow_location,RGB)         # choice RGB,the initial picture is not the RGB.
    del map_draw                                    # the example  of ImageDraw document have this 'del' step, but not know why.
    open_image.save('map/map%d.png'%imagename ,'png')                # save
    minites = int(minites) + 30
    if minites == 35:
        minites = '35'
        imagename = imagename + 1
    if minites == 65 :
        hours = hours + 1
        minites = '05'
        imagename += 1
'''

# if need , can show the shape of png data.
'''
pngdata = np.array(Image.open('map1.png'))
print pngdata.shape
print pngdata.dtype
print pngdata
'''
 