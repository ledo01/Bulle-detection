import numpy as np
import matplotlib.pyplot as plt
import os
from math import sqrt
from skimage import feature,data, io,filters
from skimage.color import rgb2gray

filename = os.path.join('img.png')
im_color = io.imread(filename)
im = rgb2gray(im_color)
im = im[550:750,860:1050]
# im[30:145,70:125] = 0
# Compute the Canny filter for two values of sigma
edges1 = feature.canny(im,1)
y,x = np.where(edges1 == True)
# display results


plt.imshow(im,cmap='RdGy')
#ax1.axis('off')
#ax1.set_title('original image', fontsize=20)

plt.scatter(x,y,c='k')
plt.show()
