#occurrence
import pytest
import logging
logger = logging.getLogger()
def  fun1(str1):
    
    str2 = ''
    dictn = {}
    
    str1 = 'I am Sipra Das'
    for i in str1.lower():
        ctr = 0
        if i not in str2 and i != ' ':

            for j in str1.lower():
                if i ==j:
                    ctr = ctr+1
                    str2 = str2+i
            dictn[i] = ctr
    return dictn




def fun2(str1):
    
    lst = str1.split()[::-1]
    str2 = (' '.join(lst))
    return str2.strip()

#i is 2 a is 3 m is 1 s is 2 p is 1 r is 1 d is 1 


@pytest.mark.parametrize("a,b,c",[("I am Sipra Das",{'i':2,'a':3,'m':1,'s':2,'p':1,'r':1,'d':1}, "Das Sipra am I")])
def test_1(a,b,c):
    logger.info("starting the function2")
    obj1= fun1(a)
    logger.info("comparion for func1")
    assert (obj1) == b

    obj2 = fun2(a)
    logger.info("comparion for func2")
    assert obj2 == c


