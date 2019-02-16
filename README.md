### I tried to obtain prime numbers using Cython with OpenMP.
```bash
#Cython compile
python setup.py build_ext --inplace

#using Cython with OpenMP
python test_c.py

#normal python
python test.py
```

#### Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz x 12
* obtain prime numbers up to 10000000
* test_c.py -> 0.79 sec
* test.py   -> 106.2 sec
* Test_c.py is 134 times faster than test.py.
