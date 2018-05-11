# __coding:utf-8__
'''
@Author  : Sun
@Time    :  下午7:10
@Software: PyCharm
@File    : routes.py
'''

import re
from common.dbtools import DatabaseAgent, sqlalchemy_session
from common.common import to_json
from common.decorators import req_params_inact
from job.models.python import Python,PythonCompany,PythonWord
from job.models.suanfa import Suanfa,SuanfaCompany,SuanfaWord
from job.models.tongxin import Tongxin,TongxinCompany,TongxinWord
from flask import request, Blueprint

api = Blueprint('api', __name__)

model_map_job = {
    "python": Python,
    "suanfa":Suanfa,
    "tongxin":Tongxin
}
model_map_com = {
    "python":PythonCompany,
    "suanfa":SuanfaCompany,
    "tongxin":TongxinCompany
}

def get_money(money):
    if money=="面议":
        return None
    else:
        pattern = re.compile(r'/d+-/d+')
        money = pattern.match(money)
        print(money)
        money = money.split('-')

@api.route("/all_money", methods=['post'])
def all():
    res = {}
    res["job"] = {}
    res["company"] = {}

    db_agent = DatabaseAgent()
    for key,job_model in model_map_job.items():
        job = db_agent.get(
            orm_model=job_model,
            all=True
        )
        res["job"][key] = len(job)
    for key,com_model in model_map_com.items():
        count = db_agent.get(
            orm_model=com_model,
            all=True
        )
        res["company"][key] = len(count)
    return to_json(200, res)
