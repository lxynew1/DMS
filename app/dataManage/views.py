from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from flask_login import login_required, logout_user
from . import datamanage
# from .forms import LoginForm
from ..models import User


@datamanage.route('/datamanage')
def landSellAdder():
    return render_template('dataManage/land_sell_adder.html')
