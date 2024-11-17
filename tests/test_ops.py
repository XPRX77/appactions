from source.math_ops import add, sub

def test_add():
    assert add(2,3) ==5
    assert add(-1,1)==0
    assert add(10,1)==11
    assert add(31,1)==32
    assert add(11,1)==12
    

def test_sub():
    assert sub(5,3) ==2
    assert sub(10,3) ==7
    assert sub(15,3) ==13
    assert sub(2,3) == -1




