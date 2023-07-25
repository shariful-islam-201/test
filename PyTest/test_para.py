import pytest


# @pytest.fixture(params=["a",'b'])
# def d_fixture(request):
#    print(request.param)


# def testItem(d_fixture):
#    print("testing")


@pytest.mark.parametrize("a,b,result", [(2, 3, 5), (4, 6, 10), (6, 1, 7)])
def testAdd(a, b, result):
    assert a + b == result
