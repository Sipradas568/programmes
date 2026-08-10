import pytest

@pytest.fixture

def setup():
    print("setup")
    yield
    print("tear down")


def test_add():
    print("add")



def test_sub(setup):
    print("substraction")

