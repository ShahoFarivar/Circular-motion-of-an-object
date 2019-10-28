# To calulate motion of a planet rotating around sun, we can use this code.
# x and y coordination of the object is in polar system.

import math

x_center=0 
y_center=0 
radius=10
location=[]
tmp={}

def to_radian(deg):
    return (math.pi/180)*deg

def orbit():
    i=0
    coor={'x':0,'y':0}
    while(i<360):
        angle_in_radian=to_radian(i)
        coor['x']=x_center+radius*math.cos(angle_in_radian)
        coor['y']=y_center+radius*math.sin(angle_in_radian)
        i+=1
        yield coor

while True:
    calculate_motion=orbit()
    for i in calculate_motion:
        location.append(i)
        tmp=location[0]
        x=tmp['x']
        y=tmp['y']
        print("x= ", x,", y= ",y) #you can use x and y to move an object