# this is the library of methods for recovery of substructures
import numpy as np
import scipy as sp
import vaex as vx
import healpy as hp

def Matched_filter(grid,binsize=[0.1,0.2],Template,Background):

	# for this method, a 2D distribution (Template) is needed. Background is also necessary before
	# calling this function. The binsize is also needed, if not, the default values will be used.
	# the algorithm is used following Equation 2 in Rockosi et al 2002
	
	shape_g = shape(grid)
	shape_T = shape(Template)
	shape_B = shape(Background)
	if (shape_B==shape_T) and (shape_T==shape_g):
		ind = grid>0
		# term 1 is the sum term
		T1 = np.sum(Template[ind]*1.0/Background[ind])
		# T2 is the integration of template
		T2 = np.sum(Template*binsize[0]*binsize[1])
		# T3 is the integration of T**2/B
		T3 = np.sum(Template**2/Background*binsize[0]*binsize[1])
		return (T1-T2)/T3
	else:
		print("The shapes of the grid, Template and Background are not consistent.")
		return 0
