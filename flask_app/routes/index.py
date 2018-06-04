# __coding:utf-8__
'''
@Author  : Sun
@Time    :  下午7:10
@Software: PyCharm
@File    : routes.py
'''

import re
from common.dbtools import DatabaseAgent, sqlalchemy_session
from common.common import to_json, Get_Average
from common.decorators import req_params_inact
from job.models.python import Python, PythonCompany, PythonWord
from job.models.suanfa import Suanfa, SuanfaCompany, SuanfaWord
from job.models.tongxin import Tongxin, TongxinCompany, TongxinWord
from flask import request, Blueprint

api = Blueprint('api', __name__)

model_map_job = {
    "python": Python,
    "suanfa": Suanfa,
    "tongxin": Tongxin
}
model_map_com = {
    "python": PythonCompany,
    "suanfa": SuanfaCompany,
    "tongxin": TongxinCompany
}


def get_money(money):
    if "面议" in money:
        return None
    elif "以" not in money:
        try:
            pattern = re.compile(r'\d+-\d+')
            money = pattern.match(money)
            money_ave = int(Get_Average(list(map(int, money.group(0).split('-')))))
            return money_ave
        except:
            print(money)
            return None


@api.route("/all", methods=['get'])
def all():
    res = {}
    res["job"] = {}
    res["company"] = {}
    res["money_ave"] = {}
    db_agent = DatabaseAgent()
    for key, job_model in model_map_job.items():
        jobs = db_agent.get(
            orm_model=job_model,
            just_first=False
        )
        money_list = []
        for job in jobs:
            money_list.append(get_money(job.money))
        res["money_ave"][key] = int(Get_Average(list(filter(None, money_list))))
        res["job"][key] = len(jobs)
    for key, com_model in model_map_com.items():
        count = db_agent.get(
            orm_model=com_model,
            just_first=False
        )
        res["company"][key] = len(count)
    return to_json(200, res)


@api.route("/job_money", methods=['post'])
@req_params_inact(
    params=('jobname',))
def job_money():
    data = request.json
    res = {}
    db_agent = DatabaseAgent()
    jobs = db_agent.get(
        orm_model=model_map_job.get(data["jobname"], None),
        just_first=False
    )
    res["money_0_5"] = []
    res["money_5_10"] = []
    res["money_10_15"] = []
    res["money_15_20"] = []
    res["money_20_30"] = []
    res["money_30_40"] = []
    res["money_40_50"] = []
    res["money_50_60"] = []
    res["money_60"] = []
    money1 = 0
    money2 = 0
    money3 = 0
    money4 = 0
    money5 = 0
    money6 = 0
    money7 = 0
    money8 = 0
    money9 = 0
    for job in jobs:
        money = get_money(job.money)
        if money == None:
            continue
        if money <= 5000:
            money1 = money1+1
        elif money <= 10000:
            money2 = money2+1
        elif money <= 15000:
            money3 = money3+1
        elif money <= 20000:
            money4 = money4+1
        elif money <= 30000:
            money5 = money5+1
        elif money <= 40000:
            money6 = money6+1
        elif money <= 50000:
            money7 = money7+1
        elif money <= 60000:
            money8 = money8+1
        else:
            money9 = money9+1
    res["money_0_5"].append(money1)
    res["money_5_10"].append(money2)
    res["money_10_15"].append(money3)
    res["money_15_20"].append(money4)
    res["money_20_30"].append(money5)
    res["money_30_40"].append(money6)
    res["money_40_50"].append(money7)
    res["money_50_60"].append(money8)
    res["money_60"].append(money9)

    return to_json(200, res)
