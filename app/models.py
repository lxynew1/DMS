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
    NOTICE_NUM = db.Column(db.String(50), unique=True, nullable=False, comment='公告编号')
    LAND_LOCATION = db.Column(db.String(255), nullable=False, comment='位置')
    TOTAL_AREA = db.Column(db.Float, nullable=False, comment='总面积（平方米）')
    CONSTRUCTION_AREA = db.Column(db.Float, nullable=True, comment='建设用地面积（平方米）')
    PLAN_BUILD_AREA = db.Column(db.Float, nullable=False, comment='规划建筑面积（平方米）')
    NOTICE_USE = db.Column(db.String(100), nullable=False, comment='公告用途')
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
