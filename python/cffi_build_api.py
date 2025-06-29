# build_api.py
from cffi import FFI
ffi = FFI()

ffi.cdef("""
    double sqrt(double x);
""")
ffi.set_source("_mymath",  # generates _mymath* extension
    '#include <math.h>',
    libraries=['m'])

if __name__ == "__main__":
    ffi.compile(verbose=True)
