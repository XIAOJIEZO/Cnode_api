import pytest
import os
import sys


@pytest.fixture(scope='session')
def login():
    """
    登录
    """
    Token = 'd9256236-ee7e-42e7-9405-4aaed6c00c70'
    return Token


# 每个测试函数都运行该fixture
@pytest.fixture(autouse=True)
def AnyTime():
    print("每次运行调用的函数AnyTime")


# fixture参数化
data = ["param1", "param2"]


@pytest.fixture(scope='function', params=data)
def return_params(request):
    return request.param


# fixture作用范围测试
@pytest.fixture(scope='function')
def user_fixtures():
    print('调用成功，每个测试函数运行一次')


@pytest.fixture(scope='module')
def execution():
    print('打开浏览器')

    yield
    print("执行teardown操作")
    print("关闭浏览器")


@pytest.fixture(scope='session')
def session():
    print('每次会话只执行一次session')


# @pytest.fixture(scope='session')
# def GetCwd():
#     cwd = os.getcwd()
#     sys.path.append(cwd)
