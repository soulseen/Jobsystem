# __coding:utf-8__
'''
@Author  : Sun
@Time    :  下午9:57
@Software: PyCharm
@File    : __init__.py.py
'''

from flask import Flask

def create_app(config_name):
    app = Flask(__name__)

    from flask_app.routes.routes import api
    app.register_blueprint(api, url_prefix='/job')

    return app