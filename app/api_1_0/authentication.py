from flask import g, jsonify, request
from flask_httpauth import HTTPBasicAuth

from . import api
from .errors import forbidden
from ..models import User

INVALID_INFO = 'Invalid credentials'

auth = HTTPBasicAuth()

@auth.verify_password
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

@auth.error_handler
def auth_error():
    return unauthorized(INVALID_INFO)

# @api.before_request
# @auth.login_required
def before_request():
    if not g.current_user.is_anonymous and not g.current_user.confirmed:
        return forbidden('Unconfirmed account')

# 登录
@api.route('/login', methods=['POST'])
def login():
    # user = User.query.filter_by(email=request.json.email.data).first()
    #     if user is not None and user.verify_password(form.password.data):
    #         login_user(user, form.remember_me.data)
    #         next = request.args.get('next')
    #         if next is None or not next.startswith('/'):
    #             next = url_for('main.index')
    #         return redirect(next)
    #     flash('Invalid username or password.')
    return jsonify(request.json)

# 生成认证令牌
@api.route('/tokens/', methods=['POST'])
def get_token():
    # 防止使用旧 token 申请新 token
    if g.current_user.is_anonymous() or g.token_used:
        return unauthorized(INVALID_INFO)
    return jsonify({
        'token': g.current_user.generate_auth_token(expiration=3600),
        'expiration': 3600
    })