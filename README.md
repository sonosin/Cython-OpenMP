### I tried to obtain prime numbers using Cython with OpenMP.
```python
#Cython compile
python setup.py build_ext --inplace

#using Cython with OpenMP
python test_c.py

#normal python
python test.py
```

### Intel® Core™ i5-4300U CPU @ 1.90GHz × 4 
### obtain prime numbers up to 10000000
### test_c.py -> 3.7 sec
### test.py   -> 130.9 sec
### Test_c.py is 35 times faster than test.py.
