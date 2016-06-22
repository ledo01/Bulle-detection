# Line correction
import numpy as np
from math import sqrt

def distance(point1,point2):
    x1,y1 = point1
    x2,y2 = point2
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def find_nearest(points,k):
    p = points[k]
    prev_d = 9999
    for i in range(k+1,len(points)):
        d = distance(p,points[i])
        if d < prev_d :
            m = i
            prev_d = d
    return m


def continu(pointArray):
    contArray = []
    i = 0
    while i < len(pointArray)-1:
        i = find_nearest(pointArray,i)
        contArray.append(pointArray[i])
    return np.asarray(contArray)
