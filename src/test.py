# coding:utf-8
# obtain prime numbers
import numpy as np
import time
import argparse

# settinng argparse
parser = argparse.ArgumentParser(
            prog='test.py',
            usage='obtain prime number by nomal python',
            description='description', 
            epilog='end',
            add_help=True,
            )
 
parser.add_argument('-n', '--number', default = 10000000)
args = parser.parse_args()
print (args.number)

#start time
start=time.time()

num = int(args.number)

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
