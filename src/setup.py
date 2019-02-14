##### setup.py #####

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy
setup(
      name        = 'prime app',
      cmdclass    = {'build_ext':build_ext},
      include_dirs=[numpy.get_include()],
      ext_modules = [Extension("prime",["prime.pyx"],extra_compile_args=['-fopenmp'],extra_link_args=['-fopenmp'])]
      )

####### end ########
