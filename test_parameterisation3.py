import pytest
inp = "I am sipra"
#op = i:2 , a:2 ,m:1, s:1

def count_char(inp):
    str2= ''
    lst = []
    for i in inp.lower():
        c= 0
        if i not in str2.lower():

            for j in inp.lower():
                if i==j:
                    c = c+1
            
           
            lst.append({i:c})
            str2= str2+i
        
    return lst


@pytest.mark.parametrize("inp,op",[("hello",[{'h' : 1}, {'e' : 1} ,{'l' : 2} ,{'o' : 2}])])
def test_char(inp,op):
    obj = count_char(inp)
    assert obj==op, "error"







