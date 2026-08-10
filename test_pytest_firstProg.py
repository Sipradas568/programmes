import pytest

def test_math_add():
    assert 2+2 ==4
    print("addition")


def test_math_subs():
    assert 6-3 == 3
    print("substraction")


@pytest.mark.xfail
def test_math_mul():
    assert 6*3 == 18
    print("mul")

