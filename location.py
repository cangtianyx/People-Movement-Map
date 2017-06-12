#-*- coding=utf-8 -*-
# this file make the tranlation of pixel location and coordinates.

map_top = 87.582425,43.880358
map_bottom = 87.607835,43.756035

# every pixel means coordinate = (43.880358 - 43.756035) / 1024 = 0.00012140917968750387 = 0.0001214

# center - suzhou = 87.603915 - 87.598587 = 0.005328 / 0.0001214 = 43.88797364085668
# center - suzhou = 43.819378 - 43.8591537 = -0.0397757 / 0.0001214 = -327.64168039538714

               
def xy_location((x,y)):      # input a tuple of coordinate
    every_pixel_equal =  0.00012140917968750387
    center_x = 87.603915
    center_y = 43.819378
    center = (512,512)
    pixel_x  = (x - center_x ) / 0.00017  # in the latitude , the count is not precise, so I choice a number to repalce it.
    pixel_y  = (y - center_y ) / every_pixel_equal
    pixel_location = (center[0] + int(pixel_x), center[1] - int(pixel_y))
    return pixel_location
