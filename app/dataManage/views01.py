from flask import render_template, redirect, request, url_for, flash, json, jsonify
from flask_login import login_user
from flask_login import login_required, logout_user
from sqlalchemy import asc, desc

from app.auth.forms import RegistrationForm
from . import datamanage
from .forms import LandSellSearch
from ..models import User, DICT_REGION, DICT_LAND_USE
from ..models import LAND_SELL_INFO_TEST_LXY
from app.util import log


@datamanage.route('/landSellSearch', methods=['GET', 'POST'])
@login_required
def landSellSearch():
    form = LandSellSearch()
    # if request.method == 'POST':
    #     land_location_list = request.values.getlist("land_location")
    #     assignment_method_list = request.values.getlist("assignment_method")
    #     result = LAND_SELL_INFO_TEST_LXY.query.filter(
    #         LAND_SELL_INFO_TEST_LXY.LAND_LOCATION.in_(land_location_list)).with_entities(
    #         LAND_SELL_INFO_TEST_LXY.LAND_LOCATION, LAND_SELL_INFO_TEST_LXY.ASSIGNMENT_METHOD).all()
    #     log("LAND_LOCATION,ASSIGNMENT_METHOD:", [(row.LAND_LOCATION, row.ASSIGNMENT_METHOD) for row in result])
    #     flash('block', 'display')
    #     flash(land_location_list, 'land_location_list')
    #     return redirect(url_for('datamanage.landSellSearch'))
    # else:
    #     return render_template('dataManage/land_sell_search.html', form=form)
    return render_template('dataManage/land_sell_search.html', form=form)


@datamanage.route('/landSellSearchNoUser', methods=['GET', 'POST'])
# @login_required
def landSellSearchNoUser():
    form = LandSellSearch()
    # if request.method == 'POST':
    #     land_location_list = request.values.getlist("land_location")
    #     assignment_method_list = request.values.getlist("assignment_method")
    #     result = LAND_SELL_INFO_TEST_LXY.query.filter(
    #         LAND_SELL_INFO_TEST_LXY.LAND_LOCATION.in_(land_location_list)).with_entities(
    #         LAND_SELL_INFO_TEST_LXY.LAND_LOCATION, LAND_SELL_INFO_TEST_LXY.ASSIGNMENT_METHOD).all()
    #     log("LAND_LOCATION,ASSIGNMENT_METHOD:", [(row.LAND_LOCATION, row.ASSIGNMENT_METHOD) for row in result])
    #     flash('block', 'display')
    #     flash(land_location_list, 'land_location_list')
    #     return redirect(url_for('datamanage.landSellSearch'))
    # else:
    #     return render_template('dataManage/land_sell_search.html', form=form)
    return render_template('dataManage/land_sell_search_nouser.html', form=form)


@datamanage.route('/landSellSearchTableAdder', methods=['GET', 'POST'])
def landSellSearchTableAdder():
    column_order = ["FID", "LAND_LOCATION", "LAND_LOCATION",
                    "ASSIGNMENT_METHOD"]
    if request.method == 'POST':
        testdata = json.loads(request.get_data())
        # land_location_list = request.values.getlist("land_location")
        log("test:", testdata)
        log("test:", type(testdata))
        draw = testdata['draw']
        start = testdata['start']
        length = testdata['length']
        page = testdata['page']
        land_location_list = testdata['land_location_list']
        order = testdata['order']
        flag = False
        for v in land_location_list:
            if v == '全部':
                flag = True
        if (flag == True):
            if (order[0].get('dir') == 'desc'):
                recordsFiltered = LAND_SELL_INFO_TEST_LXY.query.filter().count()  # 记录数
                # 这边用paginate来获取请求页码的数据
                pagination = LAND_SELL_INFO_TEST_LXY.query.filter().order_by(
                    desc(column_order[order[0].get('column')])).paginate(
                    page=page, per_page=length, error_out=True)
            else:
                recordsFiltered = LAND_SELL_INFO_TEST_LXY.query.filter().count()  # 记录数
                # 这边用paginate来获取请求页码的数据
                pagination = LAND_SELL_INFO_TEST_LXY.query.filter().order_by(
                    asc(column_order[order[0].get('column')])).paginate(
                    page=page, per_page=length, error_out=True)
        else:
            if (order[0].get('dir') == 'desc'):
                recordsFiltered = LAND_SELL_INFO_TEST_LXY.query.filter(
                    LAND_SELL_INFO_TEST_LXY.LAND_LOCATION.in_(land_location_list)).count()  # 记录数
                # 这边用paginate来获取请求页码的数据
                pagination = LAND_SELL_INFO_TEST_LXY.query.filter(
                    LAND_SELL_INFO_TEST_LXY.LAND_LOCATION.in_(land_location_list)).order_by(
                    desc(column_order[order[0].get('column')])).paginate(
                    page=page, per_page=length, error_out=True)
            else:
                recordsFiltered = LAND_SELL_INFO_TEST_LXY.query.filter(
                    LAND_SELL_INFO_TEST_LXY.LAND_LOCATION.in_(land_location_list)).count()  # 记录数
                # 这边用paginate来获取请求页码的数据
                pagination = LAND_SELL_INFO_TEST_LXY.query.filter(
                    LAND_SELL_INFO_TEST_LXY.LAND_LOCATION.in_(land_location_list)).order_by(
                    asc(column_order[order[0].get('column')])).paginate(
                    page=page, per_page=length, error_out=True)
        recordsTotal = recordsFiltered
        objs = pagination.items

        # 把页面对象变成数组，用数组作为数据源
        data = []
        num = 0
        for obj in objs:
            num = num + 1
            list = [num, obj.LAND_LOCATION, obj.ASSIGNMENT_METHOD, obj.ASSIGNMENT_LIMIT, obj.DATE_BEGIN, obj.DATE_END,
                    obj.PRICE_BEGIN]
            data.append(list)
        res = {
            # 看文档 这四个都是必要的参数，还有个error可传可不传
            'draw': draw,
            'recordsTotal': recordsTotal,
            'recordsFiltered': recordsFiltered,
            'data': data,
        }
        log(jsonify(res))
        return jsonify(res)
