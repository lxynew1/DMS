import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ORA_CONNECT_STR = 'oracle://DMS:DMS@10.73.9.21/bdc'


class Config(object):
    SECRET_KEY = '6I5MFXQNUZGJD6BVI2MF'
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_TIMEOUT = 10  # 指定数据库连接池的超时时间。默认是10s。
    SQLALCHEMY_POOL_RECYCLE = 3000  # 配置连接池的 recyle 时间。默认是7200s。
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ORA_CONNECT_STR


config = {
    'development': DevelopmentConfig
}
