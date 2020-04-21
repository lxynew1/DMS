# -*- coding:utf-8 -*-
# 2020/04/14
# Create by BlackLiu
# 工具箱

from flask import Blueprint

tools = Blueprint('tools', __name__)

from . import views
