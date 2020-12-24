import sys
import os

def get_pwd():
    pwd = os.getcwd()
    sys.path.append(pwd)
get_pwd()


from tools import methods
def new_topics(login):
    paylaod = {
        "accesstoken": login,
        "title": "yj20201224-01",
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
    print(r.json())
    assert r.status_code == 200

def test_topics():
    r = topics()
    print(r.json())