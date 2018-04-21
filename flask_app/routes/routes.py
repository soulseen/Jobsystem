# __coding:utf-8__
'''
@Author  : Sun
@Time    :  下午7:10
@Software: PyCharm
@File    : routes.py
'''

from common.dbtools import DatabaseAgent
from common.common import to_json
from common.decorators import req_params_inact
from job.models.python import Python
from flask import request, Blueprint

api = Blueprint('api', __name__)

@api.route("/all",methods=['post'])
@req_params_inact(
    params=('jobname',))
def all():
    data = request.json
    db_agent = DatabaseAgent()
    count_all = db_agent.get(
        orm_model=Python,
        count=True,
        all=True
    )
    return to_json(200,{"count":count_all})