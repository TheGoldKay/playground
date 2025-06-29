# build_api.py
from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
    double sqrt(double x);
""")
ffibuilder.set_source("_mymath",  # generates _mymath* extension
    '#include <math.h>',
    libraries=['m'])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
