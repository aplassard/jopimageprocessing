import Image
import numpy as np
from scipy.misc import imsave
import cv2
tab='\t'
RED=0
GREEN=1
BLUE=2

def arrayToImage(arr):
    return Image.fromarray(np.uint16(arr))

def Imagetoarray(img):
    return np.array(img)

def getImageAsArray(path):
    return cv2.imread(path,-1)

def savearray(arr,path):
    imsave(path,arr)


