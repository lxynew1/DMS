# -*- coding:utf-8 -*-
# 2020/01/19
# Create by BlackLiu
# 注册管理路由

from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import views
