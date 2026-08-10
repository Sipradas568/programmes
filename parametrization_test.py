import pytest

@pytest.fixture(params = ["chrome","edge"])

def login(request):
    print("setup")
    print(request.param)
    yield
    print("tear down")



def test_login(login):
    assert 2+2 == 4 , "error_fail"


