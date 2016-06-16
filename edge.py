import numpy as np
import matplotlib.pyplot as plt
import os
from skimage import feature,data, io
from skimage.color import rgb2gray
from math import sqrt

# def distance(point1,point2):
#     x1,y1 = point1
#     x2,y2 = point2
#     return sqrt((x2-x1)**2 + (y2-y1)**2)
#
# def trim(array):
#     newArray = np.copy(array)
#     idx = 0
#     while idx < len(newArray) - 1:
#         p1 = newArray[idx]
#         p2 = newArray[idx + 1]
#         if distance(p1,p2) > 75:
#             newArray = np.delete(newArray,idx+1,0)
#         else:
#             idx += 1
#     return newArray

filename = os.path.join('img.png')
im_color = io.imread(filename)
im = rgb2gray(im_color)
im = im[550:750,860:1050]
# im[30:145,70:125] = 0

edges1 = feature.canny(im,1) # Compute the Canny filter
y,x = np.where(edges1 == True)
# display results
# plt.imshow(im,cmap='RdGy')
# plt.scatter(x,y,c='k')
# plt.show()

arr = np.short(list(zip(x,y)))
l = arr[np.argsort(arr[:,0])]

newArray = np.copy(l)
idx = 0
while idx < len(newArray) - 1:
    x1,y1 = newArray[idx]
    x2,y2 = newArray[idx + 1]
    if abs(y2-y1) > 20:
        newArray = np.delete(newArray,idx+1,0)
    else:
        idx += 1

plt.plot(newArray[:,0],newArray[:,1],'o')
