from flask import request, Flask, make_response, redirect, abort

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)


@app.route('/bad')
def index2():
    return '<h1>Bad Request</h1>', 400


@app.route('/response')
def index3():
    response = make_response('<h1>This document carries a cookie</h1>')
    response.set_cookie('answer', '58')
    return response


@app.route('/redirect')
def index4():
    return redirect('http://www.baidu.com')


@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)


if __name__ == '__main__':
    app.run()

