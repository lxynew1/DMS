from flask import render_template
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
    # 区县的链接数据
    r_region = DICT_REGION.query.join(DICT_HREF, DICT_REGION.REGION_CODE == DICT_HREF.REGION_CODE).with_entities(
        DICT_REGION.REGION_CODE, DICT_REGION.REGION_NAME, DICT_HREF.HREF,DICT_HREF.NAME).filter().all()
    region_dict = {}
    for i in r_region:
        region_name_href_dict = {}
        if i.REGION_CODE in region_dict:
            value_list = region_dict[i.REGION_CODE]
        else:
            value_list = []
        region_name_href_dict[i.NAME] = i.HREF
        value_list.append(region_name_href_dict)
        region_dict[i.REGION_CODE] = value_list
    print(region_dict)
    return render_template('admin/href_lib.html')
