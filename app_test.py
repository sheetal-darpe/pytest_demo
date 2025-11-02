import pytest 
from app import add, multiply, divide


def test_add():
    assert add(3,5) ==8
    assert add(-1,1) ==0
    assert add(0,0) ==0


def test_multiply():
    assert multiply(3,5) == 15
    assert multiply(2,0) ==0
   
   
def test_divide():
    assert divide(10,2) == 5
#     with pytest.raises(ValueError):
#         divide(2,0)   

# def test_fail():
#     assert add(10,2) == 5
     