from flask import Blueprint
main = Blueprint('main', __name__)

# 脚本的末尾导入，这是为了避免循环导入依赖，因为在 views.py 和 errors.py 中还要导入蓝本 main。
from . import views, errors

