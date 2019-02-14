# coding:utf-8
# obtain prime numbers in Cython using OpenMP
import numpy as np
import prime
import time

#start time
start = time.time()

num = 10000000
prime.main(num)

#end time
end = time.time()
print ('[info] TIME: ' + str(end - start) + ' seconds\n')
