import numpy as np
import matplotlib.pyplot as plt
import os
from skimage import feature,data, io
from skimage.color import rgb2gray
from math import sqrt

def distance(point1,point2):
    "Find the distance between two points"
    x1,y1 = point1
    x2,y2 = point2
    return sqrt((x2-x1)**2 + (y2-y1)**2)

filename = os.path.join('img.png')
im_color = io.imread(filename)
im = rgb2gray(im_color)
im = im[550:750,860:1050]
# im[30:145,70:125] = 0

edges1 = feature.canny(im,1) # Compute the Canny filter
y,x = np.where(edges1 == True)
courbe = np.asarray(list(zip(x,y)))
courbe = courbe[courbe[:,0].argsort()]

# i = 0
# while i < len(courbe) -1 :
#     if distance(courbe[i],courbe[i+1]) > 50:
#         courbe = np.delete(courbe,i+1,axis=0)
#     else:
#         i += 1
# xx,yy = courbe[:,0],courbe[:,1]
# plt.plot(xx,yy,'o-')
# plt.show()

# display results
# plt.imshow(im,cmap='RdGy')
# plt.scatter(x,y,c='k')
# plt.plot(x[:30],y[:30],'o-')
# plt.show()
