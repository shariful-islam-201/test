import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5

#@pytest.mark.say
#def test_say_hello():
#    print('Hello World')

@pytest.mark.xfail
def test_say_hello():
    print('Hello World')


@pytest.mark.skip
def test_say_hi():
    print('Hello World')