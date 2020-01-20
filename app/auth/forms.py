from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Length, Email, DataRequired, EqualTo, Regexp
from ..models import User


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email(), DataRequired()])
    password = PasswordField('password', validators=[Required(), DataRequired()])
    remenber_me = BooleanField('keep me logged in')
    submit = SubmitField('登录')


class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    username = StringField('Username', validators=[Length(1, 20), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                         'Usernames must have only letters,'
                                                                         'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_repeat', message='两次输入的密码不一致！')])
    password_repeat = PasswordField('password_repeat', validators=[Required()])
    submit = SubmitField('注册')

    # 自定义用户名验证器
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已注册，请选用其它名称')

    # 自定义邮箱验证器
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已注册使用，请选用其它邮箱')
