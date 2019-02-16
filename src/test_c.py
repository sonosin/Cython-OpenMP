# coding:utf-8
# obtain prime numbers in Cython using OpenMP
import numpy as np
import prime
import time
import argparse

# settinng argparse
parser = argparse.ArgumentParser(
            prog='test.py',
            usage='obtain prime number by Cython and OpenMP',
            description='description', 
            epilog='end',
            add_help=True,
            )
 
parser.add_argument('-n', '--number', default = 10000000)
args = parser.parse_args()
print (args.number)

#start time
start = time.time()

num = int(args.number)
prime.main(num)

#end time
end = time.time()
print ('[info] TIME: ' + str(end - start) + ' seconds\n')
