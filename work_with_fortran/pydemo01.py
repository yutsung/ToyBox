
import ctypes

import numpy as np

fortran_dll = ctypes.CDLL("./demo01.so")

a_string = b"Hello, World!!"
a_int = len(a_string)
some_floats = np.arange(a_int,dtype="float64")

c_a_int = ctypes.c_int(a_int)
c_some_floats = np.ctypeslib.as_ctypes(some_floats)
c_a_string = ctypes.c_char_p(a_string)

fortran_dll.sub01(ctypes.byref(c_a_int), c_some_floats, c_a_string)

print(a_int)
print(some_floats)
