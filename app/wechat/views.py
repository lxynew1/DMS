import json
from uuid import uuid1
import datetime
import time
from flask import render_template, request
from flask_login import login_required,current_user

from app import db
from . import wechat
# from .forms import LoginForm
from ..models import DICT_REGION, DICT_LAND_USE, LAND_SELL_INFO



