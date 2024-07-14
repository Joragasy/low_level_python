import os
import ctypes
import functools
from low_level_python.llp_compiler import compile
from low_level_python.llp_types import set_ctypes

def includec(c_file):
    dll_path = 'low_level_python/__llp_cdll__/'
    print(os.system('pwd'))
    if not os.path.exists(f'{c_file}.o') or True:
        compile(c_file)
    clibrary=None
    if os.path.exists(f'{dll_path}{c_file}.o'):
        try :
            clibrary = ctypes.CDLL(f'{dll_path}{c_file}.o')
        except Exception as e :
            print(e)
            return "Compilation failed"
    def decorator_includec(func):
        @functools.wraps(func)
        def wrapper_includec(*args, **kwargs):
            func.__globals__[c_file] = clibrary
            # set_ctypes(clibrary,'sayHello','char*')
            return func(*args, **kwargs)
        return wrapper_includec
    return decorator_includec

