import uuid

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config
from flask_login import LoginManager
from flask import render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

limiter = Limiter(key_func=get_remote_address)

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    limiter.init_app(app)
    login_manager.init_app(app)
    from .api import api_models
    api_models.init_app(app=app)

    with app.test_request_context():
        db.create_all()

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/', )

    from .admin import admin as task_blueprint
    app.register_blueprint(task_blueprint, url_prefix='/')

    from .dataManage import datamanage as task_blueprint
    app.register_blueprint(task_blueprint, url_prefix='/datamanage')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')

    from .calendar import calendar as calendar_blueprint
    app.register_blueprint(calendar_blueprint, url_prefix='/calendar')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from .wechat import wechat as wechat_blueprint
    app.register_blueprint(wechat_blueprint, url_prefix='/wechat')

    from .fileManage import fileManage as fileManage_blueprint
    app.register_blueprint(fileManage_blueprint, url_prefix='/fileManage')

    return app
