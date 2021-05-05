import sys
import pytest
from tools import methods


# 指定fixture，无法使用返回值
@pytest.mark.usefixtures('user_fixtures')
class Test_fixtures():
    def test_1(self):
        return

    def test_2(self):
        return


# 测试作用范围Scope=module
def test_Scope1(session):
    print('First search')


def test_Scope2(execution):
    print('Second search')


def test_Scope3(session):
    print('Third search')


"""
异常断言：为了写关于引发异常的断言，可以使用pytest.raises作为上下文管理器
如果我们要断言它抛的异常是不是预期的，比如执行：1/0,预期结果是抛异常：ZeroDivisionError: division by zero，那我们要断言这个异常，通常是断言异常的type和value值了。
这里1/0的异常类型是ZeroDivisionError，异常的value值是division by zero，于是用例可以这样设计
"""


def test_ExceptionAssertion():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1 / 0

        # 断言异常类型type
        assert excinfo.type == ZeroDivisionError

        # 断言异常value值
        assert "division by zero" in str(excinfo.value)


# skip
@pytest.mark.skip(reason='此功能不完善，需要跳过')
def test_skip1():
    return


# skipif，为True时跳过
@pytest.mark.skipif(sys.version_info > (3, 6), reason='版本低于3.6跳过')
def test_skipif():
    return


# 测试fixture参数化
def test_FixtureParameterize(return_params):
    params = return_params
    print("fixture参数化数据：" + params)


# 测试只运行标记用例
@pytest.mark.TestMark1
def test_mark1():
    print("运行TestMark1")


@pytest.mark.TestMark2
def test_mark2():
    print("运行TestMark2")


# 重复执行的用例
@pytest.mark.repeat(5)
def test_RepeatExecution():
    return
