# 封装调用方法
import requests
from tools.host_untils import get_host as host
from tools import log_until as log


class Methods(object):

    def __init__(self):
        try:
            self.host = host()
        except Exception as error:
            log.get_log().error(error)

    def get(self, path, payload=''):
        try:
            url = self.host + path

            if payload:
                r = requests.get(url, payload, timeout=5)
                log.get_log().info('url:' + str(url) + ', request:' + str(payload) + ', response：' + str(r.json()))
                return r

            else:
                r = requests.get(url)
                log.get_log().info('url:' + str(url) + ', request:' + str(payload) + ', response：' + str(r.json()))
                return r

        except Exception as error:
            log.get_log().error(error)

    def post(self, path, payload=''):
        try:
            url = self.host + path

            if payload:
                r = requests.post(url, payload)
                log.get_log().info('url:' + str(url) + ', request:' + str(payload) + ', response：' + str(r.json()))
                return r
            else:
                r = requests.post(url, payload)
                log.get_log().info('url:' + str(url) + ', request:' + str(payload) + ', response：' + str(r.json()))
                return r

        except Exception as error:
            log.get_log().error(error)
