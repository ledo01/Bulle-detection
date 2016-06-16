# Line correction
import numpy as np
from math import sqrt

def distance(point1,point2):
    x1,y1 = point1
    x2,y2 = point2
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def find_nearest(point,pointArray):
    prev_d = distance(point,pointArray[0])
    m = 0
    for i in range(len(pointArray)):
        d = distance(point,pointArray[i])
        if d < prev_d :
            m = i
    return m

def trim(array):
    idx = 0
    while idx < len(array):
        print(len(array))
        if idx < len(array):
            p1 = array[idx]
            p2 = array[idx + 1]
            if distance(p1,p2) > 100:
                array.pop(idx + 1)
            else:
                idx += 1
        else:
            break
# def continu(pointArray):
#     contArray = []
#     for i in range(len(pointArray)):
#         if len(pointArray[(i+1):]) > 1:
#             idx = find_nearest(pointArray[i],pointArray[(i+1):])
#             point = pointArray[(i+1):][idx]
#             contArray.append(point)
#     return contArray
