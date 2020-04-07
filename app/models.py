from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    head_img = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.id

    def __unicode__(self):
        return self.id


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class LAND_SELL_INFO(db.Model):
    __tablename__ = 'LAND_SELL_INFO'
    FID = db.Column(db.String(50), primary_key=True, comment='随机UUID')
    NOTICE_NUM = db.Column(db.String(100), unique=True, nullable=False, comment='公告编号')
    LAND_LOCATION = db.Column(db.String(255), nullable=False, comment='位置')
    TOTAL_AREA = db.Column(db.Float, nullable=False, comment='总面积（平方米）')
    CONSTRUCTION_AREA = db.Column(db.String(50), nullable=True, comment='建设用地面积（平方米）')
    PLAN_BUILD_AREA = db.Column(db.String(50), nullable=False, comment='规划建筑面积（平方米）')
    NOTICE_USE = db.Column(db.String(100), nullable=False, comment='公告用途')
    PLAN_USE = db.Column(db.String(100), nullable=False, comment='规划用途')
    PLAN_USE_CUSTOM = db.Column(db.String(50), nullable=False, comment='自定义用途')
    FLOOR_AREA_RATIO = db.Column(db.String(100), nullable=False, comment='容积率')
    GREENING_RATE = db.Column(db.String(50), nullable=False, comment='绿化率')
    BUSSINESS_PROPORTION = db.Column(db.String(50), nullable=False, comment='商业比例')
    BUILDING_DENSITY = db.Column(db.String(50), nullable=False, comment='建筑密度')
    ASSIGNMENT_METHOD = db.Column(db.String(50), nullable=False, comment='出让方式')
    ASSIGNMENT_LIMIT = db.Column(db.String(50), nullable=False, comment='出让年限')
    DATE_BEGIN = db.Column(db.String(50), nullable=False, comment='起始日期')
    DATE_END = db.Column(db.String(50), nullable=False, comment='截止日期')
    REGION_CODE = db.Column(db.String(50), nullable=False, comment='区县代码')
    PRICE_BEGIN = db.Column(db.Float, nullable=False, comment='起始价（万元）')
    SECURITY_DEPOSIT = db.Column(db.Float, nullable=False, comment='保证金（万元）')
    CREATE_BY = db.Column(db.String(50), nullable=False, comment='创建人')
    CREATE_TIME = db.Column(db.DateTime, nullable=False, comment='创建时间')
    MODIFIER_BY = db.Column(db.String(50), nullable=True, comment='修改人')
    MODIFIER_TIME = db.Column(db.DateTime, nullable=True, comment='修改时间')
    CRAWL_FID = db.Column(db.String(50), nullable=True, comment='爬虫的FID值')
    IS_ONE = db.Column(db.String(10), nullable=True, comment='是否为独立地块，1为是，0为否')



class LAND_SELL_INFO_TEST_LXY(db.Model):
    __tablename__ = 'LAND_SELL_INFO_TEST_LXY'
    FID = db.Column(db.String(50), primary_key=True, comment='随机UUID')
    NOTICE_NUM = db.Column(db.String(50), unique=True, nullable=False, comment='公告编号')
    LAND_LOCATION = db.Column(db.String(255), nullable=False, comment='位置')
    TOTAL_AREA = db.Column(db.Float, nullable=False, comment='总面积（平方米）')
    CONSTRUCTION_AREA = db.Column(db.Float, nullable=True, comment='建设用地面积（平方米）')
    PLAN_BUILD_AREA = db.Column(db.Float, nullable=False, comment='规划建筑面积（平方米）')
    PLAN_USE = db.Column(db.String(100), nullable=False, comment='规划用途')
    PLAN_USE_CUSTOM = db.Column(db.String(50), nullable=False, comment='自定义用途')
    FLOOR_AREA_RATIO = db.Column(db.String(50), nullable=False, comment='容积率')
    GREENING_RATE = db.Column(db.String(50), nullable=False, comment='绿化率')
    BUSSINESS_PROPORTION = db.Column(db.String(50), nullable=False, comment='商业比例')
    BUILDING_DENSITY = db.Column(db.String(50), nullable=False, comment='建筑密度')
    ASSIGNMENT_METHOD = db.Column(db.String(50), nullable=False, comment='出让方式')
    ASSIGNMENT_LIMIT = db.Column(db.String(50), nullable=False, comment='出让年限')
    DATE_BEGIN = db.Column(db.String(50), nullable=False, comment='起始日期')
    DATE_END = db.Column(db.String(50), nullable=False, comment='截止日期')
    REGION_CODE = db.Column(db.String(50), nullable=False, comment='区县代码')
    PRICE_BEGIN = db.Column(db.Float, nullable=False, comment='起始价（万元）')
    SECURITY_DEPOSIT = db.Column(db.Float, nullable=False, comment='保证金（万元）')
    CREATE_BY = db.Column(db.String(50), nullable=False, comment='创建人')
    CREATE_TIME = db.Column(db.DateTime, nullable=False, comment='创建时间')
    MODIFIER_BY = db.Column(db.String(50), nullable=True, comment='修改人')
    MODIFIER_TIME = db.Column(db.DateTime, nullable=True, comment='修改时间')
    CRAWL_FID = db.Column(db.String(50), nullable=True, comment='爬虫唯一值，一般为官网FID')
    IS_ONE = db.Column(db.String(10), nullable=True, comment='是否为独立地块，1为是，0为否')

#土地地块详细信息
class LAND_PARCEL_DETAIL(db.Model):
    __tablename__ = 'LAND_PARCEL_DETAIL'
    FID = db.Column(db.String(50), primary_key=True, comment='随机UUID')
    PARENT_FID = db.Column(db.String(50), nullable=False, comment='公告编号ID')
    PARCEL_NO = db.Column(db.String(50), nullable=False, comment='公告编号ID')
    TOTAL_AREA = db.Column(db.Float, nullable=False, comment='总面积（平方米）')
    PLAN_BUILD_AREA = db.Column(db.String(50), nullable=False, comment='规划建筑面积（平方米）')
    PLAN_USE = db.Column(db.String(100), nullable=False, comment='规划用途')
    FLOOR_AREA_RATIO = db.Column(db.String(50), nullable=False, comment='容积率')
    GREENING_RATE = db.Column(db.String(50), nullable=False, comment='绿化率')
    BUILDING_DENSITY = db.Column(db.String(50), nullable=False, comment='建筑密度')
    ASSIGNMENT_LIMIT = db.Column(db.String(50), nullable=False, comment='出让年限')
    CREATE_BY = db.Column(db.String(50), nullable=False, comment='创建人')
    CREATE_TIME = db.Column(db.DateTime, nullable=False, comment='创建时间')
    MODIFIER_BY = db.Column(db.String(50), nullable=True, comment='修改人')
    MODIFIER_TIME = db.Column(db.DateTime, nullable=True, comment='修改时间')

class LAND_SELL_DEAL(db.Model):
    __tablename__ = 'LAND_SELL_DEAL'
    FID = db.Column(db.String(50), primary_key=True, comment='随机UUID')
    PARENT_FID = db.Column(db.String(50), nullable=False, comment='公告编号ID')
    DEAL_PRICE = db.Column(db.Float, nullable=False, comment='成交价（万元）')
    DEAL_ASSIGNMENT_METHOD = db.Column(db.String(50), nullable=False, comment='出让方式')
    DATE_DEAL = db.Column(db.String(50), nullable=False, comment='成交日期')
    CREATE_BY = db.Column(db.String(50), nullable=False, comment='创建人')
    CREATE_TIME = db.Column(db.DateTime, nullable=False, comment='创建时间')
    MODIFIER_BY = db.Column(db.String(50), nullable=True, comment='修改人')
    MODIFIER_TIME = db.Column(db.DateTime, nullable=True, comment='修改时间')



class USER_CALENDAR(db.Model):
    __tablename__ = 'USER_CALENDAR'
    id = db.Column(db.String(50), primary_key=True)
    UID = db.Column(db.String(50), db.ForeignKey('users.id'), comment='用户ID')
    TITLE = db.Column(db.String(2000), nullable=True, comment='记录日志事件')
    START = db.Column(db.String(2000), nullable=True, comment='记录开始时间')
    END = db.Column(db.String(2000), nullable=True, comment='记录结束时间')
    URL = db.Column(db.String(2000), nullable=True, comment='超链接')

    # users = db.relationship('User', backref='USER_CALENDAR')
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


class DICT_REGION(db.Model):
    __tablename__ = 'DICT_REGION'
    FID = db.Column(db.String(255), primary_key=True, comment='随机UUID')
    REGION_NAME = db.Column(db.String(255), nullable=True, comment='区县名称')
    REGION_CODE = db.Column(db.String(255), nullable=True, comment='区县代码')
    TYPE = db.Column(db.String(50), nullable=True, comment='类型')


class DICT_LAND_USE(db.Model):
    __tablename__ = 'DICT_LAND_USE'
    FID = db.Column(db.String(20), primary_key=True, comment='序号')
    USE_CODE = db.Column(db.String(50), nullable=True, comment='用途代码')
    USE_NAME = db.Column(db.String(50), nullable=True, comment='用途')
    PARENT_ID = db.Column(db.String(20), nullable=True, comment='上一级用途代码')
    GRADE = db.Column(db.String(20), nullable=True, comment='用途代码等级')

class DICT_HREF(db.Model):
    #链接库
    __tablename__ = 'DICT_HREF'
    FID = db.Column(db.String(20), primary_key=True, comment='序号')
    NAME= db.Column(db.String(50), nullable=False, comment='名称')
    HREF = db.Column(db.String(255), nullable=False, comment='链接地址')
    TYPE = db.Column(db.String(50), nullable=False, comment='类型')
    PY_PATH = db.Column(db.String(255), nullable=True, comment='监控脚本路径')
    PY_STATE = db.Column(db.String(50), nullable=True, comment='脚本开启状态，0为未开启，1为已开启')
    PY_NEXT_TIME = db.Column(db.DateTime(50), nullable=True, comment='脚本下次运行时间')
    REGION_CODE = db.Column(db.String(20), nullable=False, comment='行政区代码')

class ENTERPISE_INFO(db.Model):
    #企业信息
    __tablename__ = 'ENTERPISE_INFO'
    FID = db.Column(db.String(50), primary_key=True, comment='随机uuid')
    NAME= db.Column(db.String(50), nullable=False, comment='企业名称，请填写工商局注册的全称')
    TOP_LEVEL = db.Column(db.String(255), nullable=False, comment='所属派系')
    CREATE_BY = db.Column(db.String(50), nullable=False, comment='创建人')
    CREATE_TIME = db.Column(db.DateTime, nullable=False, comment='创建时间')
    MODIFIER_BY = db.Column(db.String(50), nullable=True, comment='修改人')
    MODIFIER_TIME = db.Column(db.DateTime, nullable=True, comment='修改时间')
    IS_FIRST = db.Column(db.String(1), nullable=True, comment='派系是否第一次创建')

class R_SELLDEAL_ENTERPISE(db.Model):
    #公告和企业的关联关系库
    __tablename__ = 'R_SELLDEAL_ENTERPISE'
    FID = db.Column(db.String(50), primary_key=True, comment='随机uuid')
    DEAL_FID= db.Column(db.String(50), nullable=False, comment='公告信息FID')
    ENTERPISE_FID = db.Column(db.String(50), nullable=False, comment='企业信息FID')
    CREATE_BY = db.Column(db.String(50), nullable=False, comment='创建人')
    CREATE_TIME = db.Column(db.DateTime, nullable=False, comment='创建时间')
    MODIFIER_BY = db.Column(db.String(50), nullable=True, comment='修改人')
    MODIFIER_TIME = db.Column(db.DateTime, nullable=True, comment='修改时间')

class FILE_PATH(db.Model):
    #文件库
    __tablename__ = 'FILE_PATH'
    FID = db.Column(db.String(50), primary_key=True, comment='随机uuid')
    TYPE = db.Column(db.String(200), nullable=False, comment='文件类型，1：软件，2：项目文档')
    TITLE= db.Column(db.String(200), nullable=False, comment='文件名称')
    DESCRIPTION = db.Column(db.String(500), nullable=False, comment='详情描述')
    PATH = db.Column(db.String(200), nullable=False, comment='系统路径')
    DOWNLOAD_TIMES = db.Column(db.Integer(), nullable=False, comment='下载次数')
    CREATE_BY = db.Column(db.String(50), nullable=False, comment='创建人')
    CREATE_TIME = db.Column(db.DateTime, nullable=False, comment='创建时间')

class GEO_PARCEL(db.Model):
    #地块坐标串
    __tablename__ = 'GEO_PARCEL'
    FID = db.Column(db.String(50), primary_key=True, comment='随机uuid')
    PARCEL_FID = db.Column(db.String(50), nullable=False, comment='地块ID')
    GEO_LIST = db.Column(db.String(2000), nullable=False, comment='列表形式的坐标串,高德直显')
    GEO_CENTER = db.Column(db.String(200), nullable=False, comment='中心点的坐标值')
    GEO_N = db.Column(db.String(200), nullable=False, comment='最北值')
    GEO_S = db.Column(db.String(200), nullable=False, comment='最南值')
    GEO_W = db.Column(db.String(200), nullable=False, comment='最西值')
    GEO_E = db.Column(db.String(200), nullable=False, comment='最东值')
    GEO_JSON = db.Column(db.String(2000), nullable=True, comment='JSON形式的坐标串')
    CREATE_BY = db.Column(db.String(50), nullable=False, comment='创建人')
    CREATE_TIME = db.Column(db.DateTime, nullable=False, comment='创建时间')
    MODIFIER_BY = db.Column(db.String(50), nullable=True, comment='修改人')
    MODIFIER_TIME = db.Column(db.DateTime, nullable=True, comment='修改时间')



