#coding:utf-8
#prime.pyx
from cython.parallel import prange
import numpy as np
cimport numpy as np

cdef extern from "math.h":
	double sqrt(double x) nogil

cdef char scheck(int n) nogil:
	cdef int i
	for i in xrange(2,int(sqrt(n)+1)):
		if n%i ==0 : return 'n'
	return 'y'

cpdef void main(int num):
	cdef np.ndarray[np.int_t,ndim=1]prime
	cdef np.ndarray[np.int_t,ndim=1]non_zero
	cdef int i, j
	prime = np.zeros(num, dtype = int)
	
	with nogil:
		for i in prange(2, num):
			if scheck(i) == 'y' :
				prime[i] = i

	non_zero = prime[np.where(prime>0)]
	print (non_zero)

