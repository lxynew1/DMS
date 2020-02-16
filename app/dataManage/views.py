from flask import render_template, redirect, request, url_for, flash, json, jsonify
from flask_login import login_user
from flask_login import login_required, logout_user
from sqlalchemy import asc, desc

from app.auth.forms import RegistrationForm
from . import datamanage
from .forms import LandSellSearch
from ..models import User, DICT_REGION, DICT_LAND_USE
from ..models import LAND_SELL_INFO_TEST_LXY
from app.util import log


@datamanage.route('/land_sell_adder', methods=['GET', 'POST'])
@login_required
def landSellAdder():
    # 添加分区信息
    r_region = DICT_REGION.query.filter(DICT_REGION.TYPE != '0').all()
    region_dict = {}
    for i in r_region:
        region_dict[i.REGION_CODE] = i.REGION_NAME

    # 添加标准用途分类信息
    r_standard_use = DICT_LAND_USE.query.filter(DICT_LAND_USE.GRADE == '1').all()
    standard_user_dict = {}
    for i in r_standard_use:
        standard_user_dict[i.USE_CODE] = i.USE_NAME

    return render_template('dataManage/land_sell_adder.html',
                           region_dict=region_dict,
                           standard_user_dict=standard_user_dict)

