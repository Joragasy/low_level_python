import pytest
from low_level_python.llp_wrapper import includec 
from low_level_python.llp_types import types

@includec("clibrary")
def c_func(**kwargs): 
    sayHello = clibrary.sayHello
    sayHello.restype = types["char*"]
    return sayHello()

def test_compile_run():
    assert c_func() == b'Hello, World!'