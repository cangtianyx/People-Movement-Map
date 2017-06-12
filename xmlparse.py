# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 02:11:00 2017

@author: ldy
"""
from xml.etree import ElementTree as ET

filename = 'none'  # chioce your data's file name

def location_data():
    global filename 
    tree = ET.parse(filename)
    root = tree.getroot()
    location_num = []
    for num in range(127) :                                  
        # the whole 'road' data's amount is 131 and there are three road has no data. so just minus 4.
        # get the midian of the string of polyline coordianta data. [6] means the tag 'polyline'
        midian = (len(root[3][2][num][6].text.split(';'))/2)
        road_location = root[3][2][num][6].text.split(';')[midian]  
        road_location = tuple(eval(road_location))       # tranlate the str to tuple
        location_num.append(road_location)
    return location_num                   # return a list of coordinate tuple


def road_direction():
    global filename
    tree = ET.parse(filename)
    root = tree.getroot()
    angle_list = []
    for num in range(127) :                                  
        angle = root[3][2][num][3].text
        angle = int(angle)
        if angle >= 315 or angle < 45 :
            direction = 'right'
            angle_list.append(direction)
        elif angle >= 45 and angle < 135 :
            direction = 'up'
            angle_list.append(direction)
        elif angle >= 135 and angle < 225 :
            direction = 'left'
            angle_list.append(direction)
        elif angle >= 225 and angle < 315 :
            direction = 'down'
            angle_list.append(direction)
    return angle_list    

def road_status():
    global filename
    tree = ET.parse(filename)
    root = tree.getroot()
    status_list = []
    for num in range(127):
        status = root[3][2][num][1].text
        status = int(status)
        status_list.append(status)
    return status_list

'''
filename = '06-09 00-05.xml'
tree = ET.parse(filename)
root = tree.getroot()
angle_list = []        
angle = root[3][2][1][3].text
direction = ''
print type(angle)
if angle >= 45 and angle < 135 :
    direction = 'up' 
    angle_list.append(direction)       
print direction,angle_list
'''

''' # findall can get the whole data down the path
p = tree.findall(r'./*/roads/road')
for a in p:
        for b in list(a):
            print b.text
            print b.tag,':',b.text
'''
'''    
        print len(root[3][2])                                                                  # the amount of 'road'
        print root[3][2][1][6].text                                                           #can find the 'polyline' by subscript
        print root[3][2][1][6].text.split(';')                                                 # split the polyline data
        print len(root[3][2][1][6].text.split(';'))                                           # the amount of data
        print root[3][2][1][6].text.split(';')[(len(root[3][2][1][6].text.split(';'))/2)]    # the image's location
'''