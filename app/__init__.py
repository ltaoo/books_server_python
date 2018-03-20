from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# 登录功能
from flask_login import LoginManager
from config import config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    # 附加路由和自定义的错误页面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # auth 蓝本
    from .auth import auth as auth_blueprint
    # /login 路由会注册成 /auth/login
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    # api 蓝本
    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    # 登录功能
    login_manager.init_app(app)

    return app
