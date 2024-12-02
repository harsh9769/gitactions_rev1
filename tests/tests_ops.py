from src.math_ops import add,sub



def test_add():

    assert add(4,5)==9
    assert add(5,5)==10

def test_sub():

    assert sub(4,5)==-1
    assert sub(5,5)==0


