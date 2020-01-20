from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from flask_login import login_required, logout_user
from . import datamanage
# from .forms import LoginForm
from ..models import User,DICT_REGION


@datamanage.route('/land_sell_adder')
@login_required
def landSellAdder():
    r = DICT_REGION.query.filter(DICT_REGION.TYPE!='0').all()
    region_dict={}
    for i in r:
        region_dict[i.REGION_CODE]=i.REGION_NAME
    print(region_dict)
    return render_template('dataManage/land_sell_adder.html',region_dict=region_dict)
