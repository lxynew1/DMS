# -*- coding:utf-8 -*-
# 2020/01/19
# Create by BlackLiu
# 注册管理路由:主要包括首页、链接库、

from flask import Blueprint

datamanage = Blueprint('datamanage', __name__)

from . import view_land_info,views01,view_enterprise,view_land_deal
