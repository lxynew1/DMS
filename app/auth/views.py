from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from flask_login import login_required, logout_user
from . import auth
from .forms import LoginForm
from ..models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        # User.password(form.password.data)
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('admin.home'))
        else:
            flash('无效的用户名密码', 'err')
            return redirect(url_for('auth.login'))
    else:
        return render_template('auth/authentication-signin.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You Have Been Logged Out.')
    return redirect(url_for('auth.login'))


@auth.route('/index')
def index():
    return 'hello me'


# 保护路由，未认证的用户访问这个路由，Flask-Login会拦截请求，把用户发送到这个页面
@auth.route('secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
