# -*- coding=utf-8 -*-
import numpy as np
top = []

def arrow((x,y),size=10, direction='down'):
    global top
    top = []  #initial top list
    top.append((x,y))
    size = np.arange(size)
    rowswidth = []   # this list shows that anyone of rows and what's the width
    colswidth = []   # like rowswidth
    if direction == 'down':
		for height in size:
			top.append((x,y - height))
			if (y+height)%2 == 1:  # every 2 rows have one generation width.
				rowswidth = np.arange((height + 1) * 2 - 1) 
			for width in rowswidth:
					top.append((x - width / 5, y - height - 1)) # division can auto to control the angle of triangle
					top.append((x + width / 5, y - height - 1))
    elif direction == 'up':
        for height in size:
            top.append((x,y + height))
            if (y+height)%2 == 1:  # every 2 rows have one generation width.
               rowswidth = np.arange((height + 1) * 2 - 1) 
            for width in rowswidth:
					top.append((x - width / 5, y + height + 1)) # division can auto to control the angle of triangle
					top.append((x + width / 5, y + height + 1))
    elif direction == 'left':
        for height in size:
            top.append((x + height,y))
            if (x+height)%2 == 1: 
                colswidth = np.arange((height + 1) * 2 - 1) 
            for width in colswidth:
					top.append((x + height + 1, y - width /6)) 
					top.append((x + height + 1, y + width /6))
    elif direction == 'right':
        for height in size:
            top.append((x - height,y))
            if (x+height)%2 == 1: 
                colswidth = np.arange((height + 1) * 2 - 1) 
            for width in colswidth:
					top.append((x - height - 1, y - width /6)) 
					top.append((x - height - 1, y + width /6)) 
    return top

