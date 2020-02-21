import json

from flask import render_template, request
from flask_login import login_required

from app import db
from . import admin
# from .forms import LoginForm
from ..models import DICT_HREF, DICT_REGION


@admin.route('/home')
@login_required
def home():
    db.create_all()
    return render_template('headers.html')


# 链接库
@admin.route('/href_lib')
@login_required
def hrefLib():
    return render_template('admin/href_lib.html')


@admin.route('/api/href_lib/region_data')
@login_required
def hrefLibRegionData():
    return_dict = {'return_code': '200', 'return_info': '', 'result': True}
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'
        return json.dumps(return_dict, ensure_ascii=False)  # ensure_ascii=False才能输出中文
    # 获取传入的参数
    get_data = request.args.to_dict()
    region_name = get_data.get("region_name")
    print(region_name)
    r_region = DICT_REGION.query.join(DICT_HREF, DICT_REGION.REGION_CODE == DICT_HREF.REGION_CODE).with_entities(
        DICT_REGION.REGION_CODE, DICT_REGION.REGION_NAME, DICT_HREF.HREF, DICT_HREF.NAME).filter(
        DICT_REGION.REGION_NAME == region_name).all()
    region_data = {}
    for i in r_region:
        region_name_href_dict = {}
        if i.REGION_NAME in region_data:
            value_list = region_data[i.REGION_NAME]
        else:
            value_list = []
        region_name_href_dict[i.NAME] = i.HREF
        value_list.append(region_name_href_dict)
        region_data[i.REGION_NAME] = value_list

    if return_dict:
        return_dict['return_info'] = region_data
    else:
        return_dict['return_code'] = '1000'
        return_dict['return_info'] = '未查询到相关数据！'
        return_dict['result'] = False
    print(return_dict)

    return json.dumps(return_dict, ensure_ascii=False)
