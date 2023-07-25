import pytest

#@pytest.fixture(autouse=True)
#@pytest.fixture(autouse=False,scope="session")
#@pytest.fixture(autouse=True,scope="function")
#@pytest.fixture(autouse=True,scope="class")
#def setUp():
#    print("launch")
#    print("login")
#    print("browse")
#    yield
#    print("logout")
#    print("closing")





@pytest.fixture(autouse=True,scope="class")
def setUp(browser):
    if browser == "chrome":
        print("Chrome")
    elif browser == "firefox":
        print("Firefox")
    print("launch")
    print("login")
    print("browse")
    yield
    print("logout")
    print("closing")




def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(autouse=True,scope="class")
def browser(request):
    return request.config.getoption("--browser")