import sys
import os

def get_pwd():
    pwd = os.getcwd()
    sys.path.append(pwd)
get_pwd()

import pytest
from tools import methods
from tools.file_untils import parse_json_file as Json

get_topics = Json('topics.json', 'get_topics')
@pytest.mark.parametrize("payload, description", get_topics)
def test_get_topics(payload, description):
    r = methods.Methods().get(r'/api/v1/topics', payload)
    assert r.json()["data"][0]["tab"] == payload["tab"]


get_topics_abnormal = Json('topics.json', 'get_topics_abnormal')
@pytest.mark.parametrize("payload, response, description", get_topics_abnormal)
def test_topics_abnormal(payload, response, description):
    r = methods.Methods().get(r'/api/v1/topics', payload)
    assert r.json()['data'] == response
