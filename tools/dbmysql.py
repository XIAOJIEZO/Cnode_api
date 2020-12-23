"""连接数据库"""
import pymysql
import tools.log_until as log
import configparser

def mysql(sql):
    try:
        config = configparser.ConfigParser()
        path = r'confglobal/confenv.ini'
        # path = r'../confglobal/confenv.ini'
        config.read(path)
        # 打开数据库连接
        db = pymysql.connect(config['mysql']['host'], config['mysql']['user'], config['mysql']['password'])
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL
        cursor.execute(sql)
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        # 关闭数据库连接
        db.close()
        log.get_log().info(sql + ':' + str(data))
        return data
    except Exception as error:
        log.get_log().error(error)
