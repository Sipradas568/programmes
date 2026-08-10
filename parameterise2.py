import pytest
#op= yes pallindrome

def pal(a):
    str2= ''
    for i in a:
        str2 = i+str2
    return str2
            
        
@pytest.mark.parametrize("a",[("121"),("231"),("1313")])
def test(a):
    obj= pal(a)
    if obj == a:
        print(f"{obj} a pallindrome")
    else:
        print(f"{obj}not  a pallindrome")



