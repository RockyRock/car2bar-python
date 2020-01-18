# Function to compute barycentric coordinates from cartesian coordinates in a hypercube
# R. Guicherd - December 2019

import numpy as np


def car2bar(car):
	"""
	Function to convert cartesian coordinates
	to barycentric coordinates in a hypercube.
	The cartesian coordinates should all be 
	bounded between zero and one.
	The function returns the barycentric
	weights that are linked to each vertices
	of the hypercube object.
	"""
	
	# Space dimension
	dim = np.shape(car)
	
	# Initialization bar variable
	bar = np.zeros((2**dim[0], 1))
	
	# Computation loop
	for i in range(2**dim[0]):
		dummy = 1
		b = np.binary_repr(i, dim[0])
		for j in range(len(b)):
			if b[j] == '1':
				dummy *= car[j]
			else:
				dummy *= (1-car[j])
		bar[i] = dummy
		
	# Function return
	return bar

