# -*- coding:utf-8 -*-
# 2020/01/19
# Create by BlackLiu
# 微信公众号界面

from flask import Blueprint

fileManage = Blueprint('fileManage', __name__)

from . import views
