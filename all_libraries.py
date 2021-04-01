from matplotlib import pyplot as plt
%matplotlib notebook
import numpy as np
from skimage.io import imread,imsave,imshow
from scipy.ndimage import distance_transform_edt
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu 
from skimage.morphology import opening,closing,disk
from skimage.segmentation import mark_boundaries
from skimage.feature import peak_local_max
from skimage.filters.rank import gradient
from skimage.measure import label
from skimage.filters import sobel 
from scipy.ndimage import distance_transform_edt
from skimage.measure import label
from skimage.measure import regionprops
from skimage.filters.rank import gradient
from skimage.morphology import watershed, disk


def loadAndPlotImage(chemin):
    im=imread(chemin)
    plt.figure()
    print(im.shape , im.dtype )
    plt.gray()
    plt.imshow(im)
    plt.show()
    
    
loadAndPlotImage("image 1.png")
loadAndPlotImage("image2.png")
loadAndPlotImage("image3.png") 
loadAndPlotImage("image4.png") 
loadAndPlotImage("image5.png")
loadAndPlotImage("image6.png") 
loadAndPlotImage("image7.png") 
loadAndPlotImage("image8.png") 
