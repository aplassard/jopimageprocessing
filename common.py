import Image
import numpy as np
from scipy.misc import imsave
tab='\t'
RED=0
GREEN=1
BLUE=2

def arrayToImage(arr):
    return Image.fromarray(np.uint16(arr))

def Imagetoarray(img):
    return np.array(img)

def getImageAsArray(path):
	im = Image.open(path)
	arr = np.zeros((im.size[1],im.size[0]),dtype=np.uint16)
	for i in xrange(arr.shape[0]):
		for j in xrange(arr.shape[1]):
				arr[i,j] = im.getpixel((j,i))
	return arr

def savearray(arr,path):
    imsave(path,arr)


