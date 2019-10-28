# To calulate motion of a planet rotating around sun, we can use this code.
# x and y coordination of the object is in polar system.

import math

def to_radian(deg):
    return (math.pi/180)*deg

x_center=0 # x position of the center of object
y_center=0 # y position of the center of object
radius=10

for i in range(360):
    angle_in_radian=to_radian(i)
    x=x_center+radius*math.cos(angle_in_radian)
    y=y_center+radius*math.sin(angle_in_radian)
    print("x= ",x,", y= ",y)

        