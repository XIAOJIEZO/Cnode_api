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