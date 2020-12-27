import pytest

@pytest.fixture()
def login():
    """
    登录
    """
    Token = 'a2c4b869-13ba-4584-85f7-d3f3b6b9c846'
    return Token

@pytest.fixture()
def user_fixtures():
    print('调用成功')