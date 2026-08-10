import pytest
def str_pall(str2):
    str1 = str2
    
    rev = ''
    for ch in str2:

        rev = ch+rev
    return rev==str1

@pytest.mark.parametrize("a,b",[("madam",True),("yes",False)])

def test_1(a,b):
    obj = str_pall(a)
    assert obj == b    
