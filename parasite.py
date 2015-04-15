#The following Python script detects malaria infected red blood cells from a jpeg image of infected red blood cells
import pylab
import Image
import scipy
from scipy import misc
from scipy import ndimage
import matplotlib.pyplot as plt
import numpy as np
import skimage
import skimage.filter, skimage.color, skimage.measure, skimage.draw, skimage.feature

orig_pylab_figsize = pylab.rcParams['figure.figsize']
bigger_pylab_figsize = 8,6
pylab.rcParams['figure.figsize'] = bigger_pylab_figsize

#cell = 'para.jpg';
#cell_image = Image.open( cell );
#cell_image.show();

#open file
cell_image = misc.imread('para.jpg')
plt.show()

#sobel filter that outlines each cell in image
bw_cell_image = skimage.color.rgb2gray(cell_image)
sobel_cell_image = skimage.filter.sobel(bw_cell_image)
plt.show(sobel_cell_image, cmap=plt.cm.gray)

#As a test: select the outline of one infected cell
print sobel_cell_image[210,250,490:530][7:10,13:18]
plt.show(sobel_beetle_image[210:250,490:530], cmap=plt.cm.gray)

#count all outlined cells

#count the pixels within the 1 outlined cell

#save this an an infected cell

#count similar cells within 1 image


