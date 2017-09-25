# this is the library of methods for recovery of substructures
import numpy as np
import scipy as sp
import vaex as vx

def Matched_filter(grid,Template,Background,binsize=[0.1,0.2]):

	# for this method, a 2D distribution (Template) is needed. Background is also necessary before
	# calling this function. The binsize is also needed, if not, the default values will be used.
	# the algorithm is used following Equation 2 in Rockosi et al 2002
	# print(np.sum(Template),'-------')
	shape_g = np.shape(grid)
	shape_T = np.shape(Template)
	shape_B = np.shape(Background)
	if (shape_B==shape_T) and (shape_T==shape_g):
		ind = (Background>0)
		# term 1 is the sum term
		T1 = np.sum(Template[ind]*1.0/Background[ind]*grid[ind])
		# T2 is the integration of template
		T2 = np.sum(Template*binsize[0]*binsize[1])
		# T3 is the integration of T**2/B
		T3 = np.sum(Template[ind]**2/Background[ind]*binsize[0]*binsize[1])
		if T3==0:
			print('-----------')
			print(Template[ind])
		# print(np.max(Background),np.min(Background))
		# print(T3,'--------')
		# print(T1,T2,T3)
		# print(np.shape(TT),np.shape(T1),np.shape(T2),np.shape(T3))
		# TT[T3>0] = (T1[T3>0]-T2)/T3[T3>0]
		# TT[ind3] = (T1[ind3]-T2[ind3])/T3[ind3]
		# wa = np.sum((T1-T2)/T3*Template[ind]*Template[ind]/Background[ind])
		return (T1-T2)/T3
	else:
		print("The shapes of the grid, Template and Background are not consistent.")
		print("shape of grid is ",np.shape(grid))
		print("shape of Template is ",np.shape(Template))
		print("shape of Background is ",np.shape(Background))
		return 0


# def get_grid2(x,y,min_x=np.min(x),max_x=np.max(x),min_y=np.min(y),max_y=np.max(y),n_x=50,n_y=50):
# 	bs_x = (max_x-min_x)/n_x
# 	bs_y = (max_y-min_y)/n_y
# 	x_array = np.linspace(min_x,max_x,n_x+1)
# 	y_array = np.linspace(min_y,max_y,n_y+1)
# 	grid = np.zeros((n_x,n_y))
# 	for i in range(0,n_x+1):
# 		for j in range(0,n_y+1):
# 			grid[i,j] = len(x[(x>x_array[i]) & (x<x_array[i+1]) & (y>y_array[j]) & (y<y_array[j+1])])

# 	return grid