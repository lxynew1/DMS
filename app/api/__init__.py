# -*- coding:utf-8 -*-
# 2020/02/13
# Create by Lxy
# 注册管理路由:api
from flask import Blueprint
from flask_restful import Api
from .items import HelloWorld

api = Blueprint('api', __name__)
# api注册到app
api_models = Api()
# 注册api路由
api_models.add_resource(HelloWorld, '/hello')

from . import items
