import sys
import os


def get_pwd():
    pwd = os.getcwd()
    sys.path.append(pwd)


get_pwd()

import pytest
from tools import methods


# 指定fixture，无法使用返回值
@pytest.mark.usefixtures('user_fixtures')
class Test_fixtures():
    def test_1(self):
        return

    def test_2(self):
        return


def test_Scope1(execution):
    print('First search')


def test_Scope2(execution):
    print('Second search')


def test_Scope3(execution):
    print('Third search')


# 异常断言，为了写关于引发异常的断言，可以使用pytest.raises作为上下文管理器
# 如果我们要断言它抛的异常是不是预期的，比如执行：1/0,预期结果是抛异常：ZeroDivisionError: division by zero，那我们要断言这个异常，通常是断言异常的type和value值了。
# 这里1/0的异常类型是ZeroDivisionError，异常的value值是division by zero，于是用例可以这样设计
def test_ExceptionAssertion():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1 / 0

        # 断言异常类型type
        assert excinfo.type == ZeroDivisionError

        # 断言异常value值
        assert "division by zero" in str(excinfo.value)
