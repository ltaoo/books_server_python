from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'

if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    manager.run()
