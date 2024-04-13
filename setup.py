from distutils.core import setup
from Cython.Build import cythonize


# compile for each cython file
setup(ext_modules =cythonize("cython1.pyx"))
setup(ext_modules =cythonize("cython2.pyx"))
setup(ext_modules =cythonize("cython3.pyx"))
setup(ext_modules =cythonize("cython4.pyx"))