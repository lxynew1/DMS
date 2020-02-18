from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from flask_login import login_required, logout_user
from . import admin
# from .forms import LoginForm
from ..models import User

from app import db


@admin.route('/home')
@login_required
def home():
    db.create_all()
    return render_template('headers.html')

#链接库
@admin.route('/href_lib')
@login_required
def hrefLib():
    return render_template('admin/href_lib.html')