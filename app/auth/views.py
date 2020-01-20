from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from flask_login import login_required, logout_user
from . import auth
from .forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash
from ..models import User
import uuid
from app import db


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        img_url = 'assets/img/tenyuan.jpg'
        print("======="+form.email.data+"=========")
        print("======="+form.username.data+"=========")
        print("======="+form.password.data+"=========")
        print("===img_url===="+img_url+"=========")
        # 根据表单数据创建用户
        user = User(id=str(uuid.uuid4()),
                 email=form.email.data,
                 username=form.username.data,
                 password_hash=str(generate_password_hash(form.password.data)),
                 head_img=img_url,
                 role_id=1)
        # 将用户保存到数据库
        db.session.add(user)
        # 自动提交
        db.session.commit()

        #跳转到主页
        flash('注册成功！', 'massage')
        return redirect(url_for('admin.home'))
    else:
        return render_template('auth/authentication-signup.html', form=form)

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
            flash(form.email.data, 'username')
            flash(form.remenber_me.data, 'checked')
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
