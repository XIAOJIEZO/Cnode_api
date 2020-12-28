import pytest

@pytest.fixture(scope='session')
def login():
    """
    登录
    """
    Token = 'a2c4b869-13ba-4584-85f7-d3f3b6b9c846'
    return Token

@pytest.fixture(scope='class')
def user_fixtures():
    print('调用成功')

# 每个测试函数都运行该fixture
@pytest.fixture(autouse=True)
def display():
    print("每次运行调用的函数")


# fixture参数化
data = ["param1", "param2"]
@pytest.fixture(scope='function', params=data)
def return_params(request):
    return request.param

