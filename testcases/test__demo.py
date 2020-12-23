import sys
import os

def get_pwd():
    pwd = os.getcwd()
    sys.path.append(pwd)
get_pwd()


from tools import methods
def topics():
    r = methods.Methods().get(r'/api/v1/topics')
    return r

def test__topics():
    r = topics()
    assert r.status_code == 200


# paylaod = {
#     "page": 9,
#     "tab": "ask",
#     "limit": 7,
# }
#
# r = Methods().get()
# print(r.text)

# h = Methods().host
# print(h)

# paylaod = {
#     "accesstoken": "a2c4b869-13ba-4584-85f7-d3f3b6b9c846",
#     "title": "yj20201223-01",
#     "tab": "ask",
#     "content": "fhsidhfospfisdjifospdfjisd"
# }
#
# r = Methods().post('/api/v1/topics', payload=paylaod)
# print(r.json())