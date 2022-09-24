from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# # html转义
# @app.route('/<path:name>')
# def hello_name(name):
#     return f'Hello {name}!'
#     # return f'Hello {escape(name)}!'


# test url_for
def test_url_for():
    with app.test_request_context():
        print(url_for('hello_name', name='world'))
        print(url_for('hello_world'))


# HTTP方法 默认是GET 可在route(methods=['GET', 'POST'])中指定
# 如果使用了GET , HEAD 和 OPTIONS 请求也会默认实现


# 渲染模板
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
