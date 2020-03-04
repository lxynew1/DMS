import datetime
import json
from uuid import uuid1

from flask import render_template, request
from flask_login import login_required, current_user

from app import db
from . import datamanage
from ..models import DICT_REGION, DICT_LAND_USE, LAND_SELL_INFO, LAND_PARCEL_DETAIL, ENTERPISE_INFO


# 企业选择列表API
@datamanage.route('/api/enterprise_info')
def enterpriseInfo():
    return_dict = {'return_code': '200', 'return_info': '', 'result': True}
    r_enterprise = ENTERPISE_INFO.query.filter().all()
    enterprise_dict = {}
    for i in r_enterprise:
        enterprise_dict[i.FID] = i.NAME
    return_dict['return_info'] = enterprise_dict
    return json.dumps(return_dict, ensure_ascii=False)


# 添加企业API
@datamanage.route('/api/add_enterprise')
def enterpriseAdder():
    return_dict = {'return_code': '200', 'return_info': '', 'result': True}
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'
        return json.dumps(return_dict, ensure_ascii=False)  # ensure_ascii=False才能输出中文
    else:
        get_data = request.args.to_dict()
        print(get_data.get("top_enterprise"))

        if get_data.get("success")=="1":
            enterprise_info = ENTERPISE_INFO(
                FID=str(uuid1()),
                NAME=get_data.get("input_enterprise_name"),
                TOP_LEVEL=get_data.get("top_enterprise"),
                IS_FIRST="0",
                CREATE_BY=current_user.id,
                CREATE_TIME=datetime.datetime.now().strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                             '%Y-%m-%d %H:%M:%S')
            )
        else:
            enterprise_info = ENTERPISE_INFO(
                FID=str(uuid1()),
                NAME=get_data.get("input_enterprise_name"),
                TOP_LEVEL=get_data.get("top_enterprise"),
                IS_FIRST="1",
                CREATE_BY=current_user.id,
                CREATE_TIME=datetime.datetime.now().strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                             '%Y-%m-%d %H:%M:%S')
            )
        try:
            db.session.add(enterprise_info)
            db.session.commit()
        except Exception as e:
            print(e)
            return_dict['return_code'] = '1000'
            return_dict['return_info'] = str(e)
            return_dict['result'] = False
    return json.dumps(return_dict, ensure_ascii=False)
