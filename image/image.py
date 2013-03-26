import numpy as np
from pylab import *
from common import *
import os

def findedges(mask):
	foundtop=False
	foundleft=False
	for i in xrange(mask.shape[0]):
		if mask[i,:].any() and not foundtop:
			top = i
			foundtop = True
		elif not mask[i,:].any() and foundtop:
			bottom = i
			break
	for i in xrange(mask.shape[1]):
		if mask[:,i].any() and not foundleft:
			left = i
			foundleft=True
		elif not mask[:,i].any() and foundleft:
			right = i
			break
	return top,bottom,left,right

class ImageClass(object):

	def __init__(self,r,g,b,nuc,myo,output='output/'):
		'''
			Container for Images
			Input:
				Red Channel Image Location
				Green Channel Image Location
				Blue Channel Image Location
				Nucleotide Mask Image Location
				Myocyte Mask Image Location
			Usage:
				>>> img = ImageClass(redfile,greenfile,bluefile,nucmask,myomask)
		'''
		print '-- Loading Red Channel --'
		self.r = getImageAsArray(r)
		print '-- Loading Green Channel --'
		self.g = getImageAsArray(g)
		print '-- Loading Blue Channel --'
		self.b = getImageAsArray(b)
		print '-- Loading Myocyte Mask --'
		self.myocytes = getImageAsArray(myo)
		print '-- Loading Nucleotide Mask --'
		self.nucleotides = getImageAsArray(nuc)
		self._path = os.path.join(os.path.abspath(os.path.dirname(__file__)),output)
		if not os.path.exists(self._path):
			print '-- Creating Directory %s --' % self._path
			os.mkdir(self._path)
		print '-- Set %s as Output Directory --' %self._path

		m,n=self.r.shape
		self.img = np.zeros([m,n,5])
		self.img[:,:,0]=self.r
		self.img[:,:,1]=self.g
		self.img[:,:,2]=self.b
		self.img[:,:,3]=self.myocytes
		self.img[:,:,4]=self.nucleotides
		self.myocyteobjects = []
		self.nucleusobjects = []
		for i in xrange(1,self.myocytes.max()):
			mask = self.myocytes == i
			top,bottom,left,right = findedges(mask)
			self.myocyteobjects.append(ImageObject(self.img[top:bottom,left:right,:],top,bottom,left,right))
			imsave(self._path+'myocyte_'+str(i)+'.tiff',self.img[top:bottom,left:right,[0,1,2]])
		for i in xrange(1,self.nucleotides.max()):
			mask = self.nucleotides == i
			top,bottom,left,right = findedges(mask)
			self.nucleusobjects.append(ImageObject(self.img[top:bottom,left:right,:],top,bottom,left,right))
			imsave(self._path+'nuclei_'+str(i)+'.tiff',self.img[top:bottom,left:right,[0,1,2]])

class ImageObject(object):

	def __init__(self,arr,top,bottom,left,right):
		pass
