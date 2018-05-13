from flask import g, jsonify, request
from flask.ext.login import logout_user, login_required
# from flask_httpauth import HTTPBasicAuth

from . import api
from .errors import forbidden
from ..models import User

INVALID_INFO = 'Invalid credentials'

# auth = HTTPBasicAuth()

# @auth.verify_password
def verify_password(email_or_token, password):
    if email_or_token == '':
        return True
    if password == '':
        g.current_user = User.verify_auth_token(email_or_token)
        g.token_used = True
        return g.current_user is not None
    user = User.query.filter_by(email = email_or_token).first()
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    return user.verify_password(password)

# @auth.error_handler
# def auth_error():
    # return unauthorized(INVALID_INFO)

# @api.before_request
# @auth.login_required
def before_request():
    if not g.current_user.is_anonymous and not g.current_user.confirmed:
        return forbidden('Unconfirmed account')

# 登录
@api.route('/login', methods=['POST'])
def login():
    userinfo = request.json
    user = User.query.filter_by(email=userinfo['email']).first()
    # 用户存在，判断密码是否正确
    if user is not None and user.verify_password(userinfo['password']):
        return jsonify({
            'c': '0',
            'm': '',
            'd': user.to_json()
        })
    return jsonify({
        'c': '-1',
        'm': '用户名或密码错误',
        'd': 'error'
    })

@api.route('/logout')
def logout():
    logout_user()
    return jsonify({
        'c': '0',
        'm': '',
        'd': ''
    })

# 生成认证令牌
# @api.route('/tokens/', methods=['POST'])
# def get_token():
#     # 防止使用旧 token 申请新 token
#     if current_user.is_anonymous() or g.token_used:
#         return unauthorized(INVALID_INFO)
#     return jsonify({
#         'token': current_user.generate_auth_token(expiration=3600),
#         'expiration': 3600
#     })