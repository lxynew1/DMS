import json

from flask import render_template, request
from flask_login import login_required
from sqlalchemy import and_, func
from collections import defaultdict

from . import fileManage
from ..global_fun import allDay, allRegion
# from .forms import LoginForm
from ..models import DICT_REGION, LAND_SELL_INFO

@login_required
@fileManage.route('/download/index')
def downloadIndex():
    return render_template('fileManage/download.html')

@login_required
@fileManage.route('/upload')
def upload():
    return render_template('fileManage/upload.html')


