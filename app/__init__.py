from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask import render_template

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name='development'):
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(config[config_name])
    db.init_app(app)
    login_manager.init_app(app)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def page_not_found(e):
        return render_template('errors/500.html'), 500

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/',)

    return app
