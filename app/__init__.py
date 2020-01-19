from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config
from flask_login import LoginManager
from flask import render_template

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    login_manager.init_app(app)
    with app.test_request_context():
        db.create_all()


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/',)

    from .admin import admin as task_blueprint
    app.register_blueprint(task_blueprint, url_prefix='/admin')

    from .dataManage import datamanage as task_blueprint
    app.register_blueprint(task_blueprint, url_prefix='/datamanage')

    return app
