from flask import jsonify, request, g, url_for, current_app

from . import api
# from .decorators import permission_required
from .errors import forbidden

from .. import db
from ..models import Book, Permission

@api.route('/books/')
def get_books():
    page = request.args.get('page', 1, type=int)
    pagination = Book.query.paginate(
        page,
        per_page = current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out = False
    )
    books = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_users', page = page - 1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_users', page = page + 1)
    return jsonify({
      'c': '0',
      'm': '',
      'd': {
        'data': [book.to_json() for book in books],
        'prev': prev,
        'next': next,
        'count': pagination.total
      }
    })


# @api.route('/posts/<int:id>')
# def get_post(id):
#     post = Post.query.get_or_404(id)
#     return jsonify(post.to_json())

# 新增用户
@api.route('/books/', methods=['POST'])
# @permission_required(Permission.WRITE)
def new_book():
    book = Book.from_json(request.json)
    db.session.add(book)
    db.session.commit()
    return jsonify({
      'c': '0',
      'm': '',
      'd': book.to_json(),
    })


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