import os
import logging

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ORA_CONNECT_STR = 'oracle://DMS:DMS@10.73.9.21/bdc'
# ORA_CONNECT_STR = 'oracle://hr:hr@114.67.240.64:1521/orcl'


class Config(object):
    SECRET_KEY = '6I5MFXQNUZGJD6BVII2MF'
    # os.environ['NLS_LANG'] = 'SIMPLFIED CHINESE_CHINA.UTF8'
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_TIMEOUT = 10  # 指定数据库连接池的超时时间。默认是10s。
    SQLALCHEMY_POOL_RECYCLE = 3000  # 配置连接池的 recyle 时间。默认是7200s。
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    max_identifier_length = 128
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY_ECHO = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ORA_CONNECT_STR


config = {
    'development': DevelopmentConfig
}
