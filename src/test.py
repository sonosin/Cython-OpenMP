# coding:utf-8
# obtain prime numbers
import numpy as np
import time

#start time
start=time.time()

num = 10000000

def scheck(n):
	flag = True
	for i in range(2,int(np.sqrt(n)) + 1):
		if n%i ==0 :
			flag = False
			break
	return flag

prime = []
for i in range(2, num):
	if scheck(i) == True:
		prime.append(i)		
print (np.array(prime))

#end time
end = time.time()
print ('[info] TIME: ' + str(end - start) + ' seconds\n')
