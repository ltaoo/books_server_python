from flask import Flask
from flask_script import Manager, Shell
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
manager = Manager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yimi@172.17.0.3:3306/books'
db = SQLAlchemy(app)


# 角色
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

# 用户表
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    tel = db.Column(db.String(120))
    address = db.Column(db.String(120))
    rank = db.Column(db.Integer)

    records = db.relationship('Record', backref='role')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

# 图书表
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    isbn = db.Column(db.String(120))
    price = db.Column(db.Float)
    address = db.Column(db.String(120))
    rank = db.Column(db.Integer)

    records = db.relationship('Record', backref='role')

    def __repr__(self):
        return '<Book %r>' % self.title

# 借阅记录表
class Record(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    # 外键
    borrow_time = db.Column(db.DateTime)
    return_time = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<Record %r>' % self.id

# 订单记录表
class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    # books = db.Column(db.Enum)
    message = db.Column(db.String(120))
    state = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Order %r>' % self.id

@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'

# 导出上下文便于使用
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    manager.run()
