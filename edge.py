import numpy as np
import matplotlib.pyplot as plt
import os
from skimage import feature,data, io
from skimage.color import rgb2gray

filename = os.path.join('img.png')
im_color = io.imread(filename)
im = rgb2gray(im_color)
im = im[550:750,860:1050]
# im[30:145,70:125] = 0

edges1 = feature.canny(im,1) # Compute the Canny filter
y,x = np.where(edges1 == True)
# display results
# plt.imshow(im,cmap='RdGy')

plt.scatter(x,y,c='k')
plt.show()
