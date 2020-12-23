# 封装调用方法
import sys
import os

def get_pwd():
    pwd = os.getcwd()
    return pwd

sys.path.append(get_pwd())

import requests
from tools.host_untils import get_host as host


class Methods:

    def __init__(self):

        self.host = host()

    def get(self, path, payload=''):
        url = self.host + path

        if payload:
            r = requests.get(url, payload)
            return r
        else:
            r = requests.get(url)
            return r

    def post(self, path, payload=''):
        url = self.host + path

        if payload:
            r = requests.post(url, payload)
            return r
        else:
            r = requests.post(url, payload)
            return r






