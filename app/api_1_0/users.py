from flask import jsonify, request, g, url_for, current_app

from . import api
# from .decorators import permission_required
from .errors import forbidden

from .. import db
from ..models import User, Permission

@api.route('/users/')
def get_users():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.paginate(
        page,
        per_page = current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out = False
    )
    users = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_users', page = page - 1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_users', page = page + 1)
    return jsonify({
        'users': [user.to_json() for user in users],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


# @api.route('/posts/<int:id>')
# def get_post(id):
#     post = Post.query.get_or_404(id)
#     return jsonify(post.to_json())


@api.route('/users/', methods=['POST'])
# @permission_required(Permission.WRITE)
def new_post():
    print(request.json)
    user = User.from_json(request.json)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json())


# @api.route('/posts/<int:id>', methods=['PUT'])
# @permission_required(Permission.WRITE)
# def edit_post(id):
#     post = Post.query.get_or_404(id)
#     if g.current_user != post.author and \
#             not g.current_user.can(Permission.ADMIN):
#         return forbidden('Insufficient permissions')
#     post.body = request.json.get('body', post.body)
#     db.session.add(post)
#     db.session.commit()
#     return jsonify(post.to_json())