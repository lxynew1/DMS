from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, current_user
from flask_login import login_required, logout_user
from . import auth
from .forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash
from ..models import User
import uuid
from app import db
import json


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        img_url = '/static/assets/img/tenyuan.jpg'
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

        # 跳转到主页
        flash('注册成功！', 'massage')
        return redirect(url_for('admin.hrefLib'))
    else:
        return render_template('auth/authentication-signup.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
@auth.route('/', methods=['GET', 'POST'])
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


@auth.route('/email_check', methods=['GET', 'POST'])
def email_check():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '', 'result': False}
    # 判断传入的参数是否为空
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'
        return json.dumps(return_dict, ensure_ascii=False)  # ensure_ascii=False才能输出中文
    # 获取传入的参数
    get_data = request.args.to_dict()
    email = get_data.get('email')
    # 对参数进行操作
    if User.query.filter_by(email=email).first():
        return_dict['return_code'] = '1000'
        return_dict['return_info'] = '邮箱已被注册'
        return json.dumps(return_dict, ensure_ascii=False)
    return json.dumps(return_dict, ensure_ascii=False)


@auth.route('/username_check', methods=['GET', 'POST'])
def username_check():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '', 'result': False}
    # 判断传入的参数是否为空
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'
        return json.dumps(return_dict, ensure_ascii=False)  # ensure_ascii=False才能输出中文
    # 获取传入的参数
    get_data = request.args.to_dict()
    username = get_data.get('username')

    # 对参数进行操作
    if User.query.filter_by(username=username).first():
        return_dict['return_code'] = '1000'
        return_dict['return_info'] = '用户名已被注册'
        return json.dumps(return_dict, ensure_ascii=False)
    return json.dumps(return_dict, ensure_ascii=False)
