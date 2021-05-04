import configparser
# import tools.log_until as log

def get_host():
    """获取配置的测试环境"""
    config = configparser.ConfigParser()
    path = r'confglobal/confenv.ini'
    config.read(path, encoding='utf-8')
    if config.get('HOST', 'port'):
        host = 'http://' + config.get('HOST', 'host') + ':' + config.get('HOST', 'port')
    else:
        host = config.get('HOST', 'host')
    return host
