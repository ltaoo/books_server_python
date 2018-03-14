from flask import render_template, session, redirect, url_for
from datetime import datetime
from . import main
from .. import db
from ..models import User

# 路由装饰器由蓝本提供
@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template(
        'index.html',
        known = session.get('known', False),
        current_time = datetime.utcnow()
    )