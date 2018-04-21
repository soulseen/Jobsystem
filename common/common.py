# _*_coding:utf-8_*_


from flask import jsonify
from .dbtools import DatabaseAgent
import jieba


MSG_MAP = {
    200: 'success',
    401: '未提供认证信息',
    402: '认证信息过期，请重新登录',
    403: '错误的认证信息',
    404: '请求内容不存在',
    405: '不允许的操作',
    410: '用户名已存在',
    421: '用户名或密码错误',
    422: '请求缺少必要参数',
    500: '请求错误，请联系管理员',
    501: 'JSON格式错误',
    10000: '目录名已存在',
    10001: '文件传输错误'
}


MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'db'
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'
MYSQL_PORT = 3306


def params_inact(post_data, *args):
    """ 验证请求是否完整 """
    if not isinstance(post_data, dict):
        return False
    for arg in args:
        if arg not in post_data.keys():
            print ("miss {} filed ".format(arg))
            return False
    return True

def to_json(code, data=None):
    """ 统一格式返回 """
    return jsonify({
        "code": code,
        "msg": MSG_MAP[code],
        "data": data
    })

def clear(data):
    return data.strip().replace('\n', '').replace('\t', '').replace('\r', '').replace(',', '').replace('.',
                                                                                                       '').replace(
        '!', '').replace('，', '').replace('。', '').replace('！', '').replace('、', '').replace(':', '').replace('：',
                                                                                                              '').replace(
        ' ', '').replace('"', '').replace('\'', '').replace('“', '').replace('”', '').replace('；', '').replace('(',
                                                                                                               '').replace(
        ')', '')

def parse_word(description,word_model):
    db_agent = DatabaseAgent()
    seg_list = jieba.cut(description)
    for x in seg_list:
        if x == " ":
            continue
        exists = db_agent.get(
            filter_kwargs={
                "word": str(x)
            },
            orm_model=word_model
        )
        if exists:
            db_agent.update(
                filter_kwargs={
                    "word": str(x)
                },
                method_kwargs={
                    "count": 1 + exists.count
                },
                orm_model=word_model
            )
        else:
            db_agent.add(
                kwargs={
                    "word": str(x),
                    "count": 1
                },
                orm_model=word_model
            )
