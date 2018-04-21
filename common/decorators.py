# __coding:utf-8__
'''
@Author  : Sun
@Time    :  下午7:57
@Software: PyCharm
@File    : decorators.py
'''

from functools import wraps, partial
from .common import params_inact, to_json
from flask import request

def req_params_inact(f=None, params=None):
    """ 验证参数齐全 """
    if f is None:
        return partial(req_params_inact, params=params)

    @wraps(f)
    def deco_func(*args):
        if not params_inact(request.json, *params):
            return to_json(422)
        return f(*args)

    return deco_func