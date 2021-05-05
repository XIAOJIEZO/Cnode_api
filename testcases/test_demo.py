from tools import methods
import pytest
import allure


def new_topics(login):
    paylaod = {
        "accesstoken": login,
        "title": "yj20201224-02",
        "tab": "ask",
        "content": "fhsidhfospfisdjifospdfjisd"
    }
    r = methods.Methods().post(r'/api/v1/topics', paylaod)
    return r


def topics():
    r = methods.Methods().get(r'/api/v1/topics')
    return r


def test_new_topics(login):
    r = new_topics(login)
    assert r.status_code == 200


def test_topics():
    r = topics()
    assert r.status_code == 200


@allure.feature("测试fixture参数化")
@allure.title("{return_params}")
@pytest.mark.mark1
def test_params(return_params):
    a = return_params
    print(a)


def test_LoginName(login):
    """
    test_LoginName
    """
    payload = {"accesstoken": login}
    r = methods.Methods().get(r'/api/v1/user/alsotang', payload=payload)
    assert r.status_code == 200
