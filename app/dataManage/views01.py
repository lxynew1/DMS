import datetime
from typing import List

# from ratelimit import limits, RateLimitException
from app import limiter
from flask import render_template, redirect, request, url_for, flash, json, jsonify
from flask_login import login_user
from flask_login import login_required, logout_user
from sqlalchemy import asc, desc, and_

from app.auth.forms import RegistrationForm
from . import datamanage
from .forms import LandSellSearch
from ..models import User, DICT_REGION, DICT_LAND_USE
from ..models import LAND_SELL_INFO
from app.util import log


@datamanage.route('/landSellSearch', methods=['GET', 'POST'])
@login_required
def landSellSearch():
    form = LandSellSearch()
    # if request.method == 'POST':
    #     land_location_list = request.values.getlist("land_location")
    #     assignment_method_list = request.values.getlist("assignment_method")
    #     result = LAND_SELL_INFO.query.filter(
    #         LAND_SELL_INFO.LAND_LOCATION.in_(land_location_list)).with_entities(
    #         LAND_SELL_INFO.LAND_LOCATION, LAND_SELL_INFO.ASSIGNMENT_METHOD).all()
    #     log("LAND_LOCATION,ASSIGNMENT_METHOD:", [(row.LAND_LOCATION, row.ASSIGNMENT_METHOD) for row in result])
    #     flash('block', 'display')
    #     flash(land_location_list, 'land_location_list')
    #     return redirect(url_for('datamanage.landSellSearch'))
    # else:
    #     return render_template('dataManage/land_sell_search.html', form=form)
    return render_template('dataManage/land_sell_search.html', form=form)


@datamanage.route('/landSellSearch01', methods=['GET', 'POST'])
def landSellSearch01():
    form = LandSellSearch()
    # if request.method == 'POST':
    #     land_location_list = request.values.getlist("land_location")
    #     assignment_method_list = request.values.getlist("assignment_method")
    #     result = LAND_SELL_INFO.query.filter(
    #         LAND_SELL_INFO.LAND_LOCATION.in_(land_location_list)).with_entities(
    #         LAND_SELL_INFO.LAND_LOCATION, LAND_SELL_INFO.ASSIGNMENT_METHOD).all()
    #     log("LAND_LOCATION,ASSIGNMENT_METHOD:", [(row.LAND_LOCATION, row.ASSIGNMENT_METHOD) for row in result])
    #     flash('block', 'display')
    #     flash(land_location_list, 'land_location_list')
    #     return redirect(url_for('datamanage.landSellSearch'))
    # else:
    #     return render_template('dataManage/land_sell_search.html', form=form)
    return render_template('dataManage/land_sell_search_nouser.html', form=form)


def objSearchValue(num: int, vlaue: str, data: List[str], obj):
    for i in obj:
        if str(i).__contains__(vlaue):
            list = [
                str(num) + " <a href='/datamanage/land_sell_deal?fid=" + obj.FID + "' target='blank' class='up btn btn-default btn-xs'><i class='fa fa-arrow-up'></i> 编辑</a>",
                obj.REGION_NAME,  # 区县代码
                obj.NOTICE_NUM,  # 公告编号
                obj.LAND_LOCATION,  # 位置
                obj.TOTAL_AREA,  # 总面积（平方米）
                obj.CONSTRUCTION_AREA,  # 建设用地面积（平方米）
                obj.PLAN_BUILD_AREA,  # 规划建筑面积（平方米）
                # obj.USE_NAME,  # 用途分类
                obj.PLAN_USE_CUSTOM,  # 自定义用途
                obj.FLOOR_AREA_RATIO,  # 容积率
                obj.GREENING_RATE,  # 绿化率
                obj.BUSSINESS_PROPORTION,  # 商业比例
                obj.BUILDING_DENSITY,  # 建筑密度
                obj.ASSIGNMENT_METHOD,  # 出让方式
                obj.ASSIGNMENT_LIMIT,  # 出让年限
                obj.DATE_BEGIN,  # 起始日期
                obj.DATE_END,  # 截止日期
                obj.PRICE_BEGIN,  # 起始价（万元）
                obj.SECURITY_DEPOSIT,  # 保证金（万元）
                # obj.CREATE_BY,  # 创建人
                # obj.CREATE_TIME,  # 创建时间
                # obj.MODIFIER_BY,  # 修改人
                # obj.MODIFIER_TIME,  # 修改时间
                obj.NOTICE_USE,  # 公告用途
                ]
            data.append(list)
            return None


@datamanage.route('/landSellSearchTableAdder', methods=['GET', 'POST'])
@limiter.limit("2/second", error_message="OverSpeed",
               exempt_when=lambda: len(str(request.get_json("search_value").get("search_value"))) != 0)
@login_required
def landSellSearchTableAdder():
    column_order = ["FID",
                    "REGION_NAME",
                    "NOTICE_NUM",
                    "LAND_LOCATION",
                    "TOTAL_AREA",
                    "CONSTRUCTION_AREA",
                    "PLAN_BUILD_AREA",
                    # "USE_NAME",
                    "PLAN_USE_CUSTOM",
                    "FLOOR_AREA_RATIO",
                    "GREENING_RATE",
                    "BUSSINESS_PROPORTION",
                    "BUILDING_DENSITY",
                    "ASSIGNMENT_METHOD",
                    "ASSIGNMENT_LIMIT",
                    "DATE_BEGIN",
                    "DATE_END",
                    "PRICE_BEGIN",
                    "SECURITY_DEPOSIT",
                    "NOTICE_USE"
                    ]
    if request.method == 'POST':
        land_search_data = json.loads(request.get_data())
        # log("land_search_data:", land_search_data)
        draw = land_search_data['draw']
        start = land_search_data['start']
        length = land_search_data['length']
        page = land_search_data['page']
        s_day = land_search_data['s_day']
        search_value = land_search_data['search_value']
        if s_day == '':
            s_day = '1900-01-01'
        else:
            mon = s_day[0:2]
            day = s_day[3:5]
            year = s_day[6:10]
            s_day = year + '-' + mon + '-' + day
        e_day = land_search_data['e_day']
        if e_day == '':
            e_day = '2300-01-01'
        else:
            mon = e_day[0:2]
            day = e_day[3:5]
            year = e_day[6:10]
            e_day = year + '-' + mon + '-' + day
        # log(e_day, s_day)
        region_name_list = [w.REGION_CODE for w in DICT_REGION.query.filter(
            DICT_REGION.REGION_NAME.in_(land_search_data['region_name_list'])).all()]
        land_location = '%' + land_search_data['land_location'] + '%'
        assignment_method_list = land_search_data['assignment_method_list']  # 出让方式
        assignment_limit_list = land_search_data['assignment_limit_list']  # 出让年限
        # plan_use_list = [w.USE_CODE for w in DICT_LAND_USE.query.filter(
        #     DICT_LAND_USE.USE_NAME.in_(land_search_data['plan_use_list'])).all()]  # 用途分类
        plan_use_list = land_search_data['plan_use_list']
        order = land_search_data['order']  # 排序方式

        # 查询条件定义
        # 行政区+公告时间+土地坐落
        if region_name_list == [] or str(region_name_list).__contains__('全部'):
            region_rules = and_(*[LAND_SELL_INFO.REGION_CODE.like(w) for w in ['%']],
                                LAND_SELL_INFO.LAND_LOCATION.like(land_location), LAND_SELL_INFO.DATE_BEGIN >= s_day,
                                LAND_SELL_INFO.DATE_END <= e_day)
        else:
            region_rules = and_(*[LAND_SELL_INFO.REGION_CODE.in_(w) for w in [region_name_list]],
                                LAND_SELL_INFO.LAND_LOCATION.like(land_location), LAND_SELL_INFO.DATE_BEGIN >= s_day,
                                LAND_SELL_INFO.DATE_END <= e_day)

        # 出让方式
        if assignment_method_list == [] or str(assignment_method_list).__contains__('全部'):
            assignment_method_rules = and_(*[LAND_SELL_INFO.ASSIGNMENT_METHOD.like(w) for w in ['%']])
        else:
            assignment_method_rules = and_(*[LAND_SELL_INFO.ASSIGNMENT_METHOD.in_(w) for w in [assignment_method_list]])

        # 出让年限
        if assignment_limit_list == [] or str(assignment_limit_list).__contains__('全部'):
            assignment_limit_rules = and_(*[LAND_SELL_INFO.ASSIGNMENT_LIMIT.like(w) for w in ['%']])
        else:
            assignment_limit_rules = and_(*[LAND_SELL_INFO.ASSIGNMENT_LIMIT.in_(w) for w in [assignment_limit_list]])

        # 用途分类
        if plan_use_list == [] or str(assignment_limit_list).__contains__('全部'):
            plan_use_rules = and_(*[LAND_SELL_INFO.PLAN_USE.like(w) for w in ['%']])
        else:
            plan_use_rules = and_(*[LAND_SELL_INFO.PLAN_USE_CUSTOM.in_(w) for w in [plan_use_list]])

        if (order[0].get('dir') == 'desc'):  # 确定排序方法
            recordsFiltered = LAND_SELL_INFO.query \
                .filter(region_rules,
                        assignment_method_rules,
                        assignment_limit_rules,
                        plan_use_rules).count()  # 记录数
            # 这边用paginate来获取请求页码的数据
            pagination = LAND_SELL_INFO.query \
                .join(DICT_REGION,
                      LAND_SELL_INFO.REGION_CODE == DICT_REGION.REGION_CODE) \
                .with_entities(
                LAND_SELL_INFO.FID,
                LAND_SELL_INFO.NOTICE_NUM,
                LAND_SELL_INFO.LAND_LOCATION,
                LAND_SELL_INFO.TOTAL_AREA,
                LAND_SELL_INFO.CONSTRUCTION_AREA,
                LAND_SELL_INFO.PLAN_BUILD_AREA,
                LAND_SELL_INFO.NOTICE_USE,
                # DICT_LAND_USE.USE_NAME,
                LAND_SELL_INFO.PLAN_USE_CUSTOM,
                LAND_SELL_INFO.PLAN_USE_CUSTOM,
                LAND_SELL_INFO.FLOOR_AREA_RATIO,
                LAND_SELL_INFO.GREENING_RATE,
                LAND_SELL_INFO.BUSSINESS_PROPORTION,
                LAND_SELL_INFO.BUILDING_DENSITY,
                LAND_SELL_INFO.ASSIGNMENT_METHOD,
                LAND_SELL_INFO.ASSIGNMENT_LIMIT,
                LAND_SELL_INFO.DATE_BEGIN,
                LAND_SELL_INFO.DATE_END,
                DICT_REGION.REGION_NAME,
                LAND_SELL_INFO.PRICE_BEGIN,
                LAND_SELL_INFO.SECURITY_DEPOSIT,
                LAND_SELL_INFO.CREATE_BY,
                LAND_SELL_INFO.CREATE_TIME,
                LAND_SELL_INFO.MODIFIER_BY,
                LAND_SELL_INFO.MODIFIER_TIME
            ).filter(region_rules,
                     assignment_method_rules,
                     assignment_limit_rules,
                     plan_use_rules) \
                .order_by(desc(column_order[order[0].get('column')])) \
                .paginate(page=page, per_page=length, error_out=True)
        else:
            recordsFiltered = LAND_SELL_INFO.query \
                .filter(region_rules,
                        assignment_method_rules,
                        assignment_limit_rules,
                        plan_use_rules).count()  # 记录数
            # 这边用paginate来获取请求页码的数据
            pagination = LAND_SELL_INFO.query \
                .join(DICT_REGION,
                      LAND_SELL_INFO.REGION_CODE == DICT_REGION.REGION_CODE) \
                .with_entities(
                LAND_SELL_INFO.FID,
                LAND_SELL_INFO.NOTICE_NUM,
                LAND_SELL_INFO.LAND_LOCATION,
                LAND_SELL_INFO.TOTAL_AREA,
                LAND_SELL_INFO.CONSTRUCTION_AREA,
                LAND_SELL_INFO.PLAN_BUILD_AREA,
                LAND_SELL_INFO.NOTICE_USE,
                # DICT_LAND_USE.USE_NAME,
                LAND_SELL_INFO.PLAN_USE_CUSTOM,
            LAND_SELL_INFO.PLAN_USE_CUSTOM,
                LAND_SELL_INFO.FLOOR_AREA_RATIO,
                LAND_SELL_INFO.GREENING_RATE,
                LAND_SELL_INFO.BUSSINESS_PROPORTION,
                LAND_SELL_INFO.BUILDING_DENSITY,
                LAND_SELL_INFO.ASSIGNMENT_METHOD,
                LAND_SELL_INFO.ASSIGNMENT_LIMIT,
                LAND_SELL_INFO.DATE_BEGIN,
                LAND_SELL_INFO.DATE_END,
                DICT_REGION.REGION_NAME,
                LAND_SELL_INFO.PRICE_BEGIN,
                LAND_SELL_INFO.SECURITY_DEPOSIT,
                LAND_SELL_INFO.CREATE_BY,
                LAND_SELL_INFO.CREATE_TIME,
                LAND_SELL_INFO.MODIFIER_BY,
                LAND_SELL_INFO.MODIFIER_TIME
            ).filter(region_rules,
                     assignment_method_rules,
                     assignment_limit_rules,
                     plan_use_rules) \
                .order_by(asc(column_order[order[0].get('column')])) \
                .paginate(page=page, per_page=length, error_out=True)

        recordsTotal = recordsFiltered
        objs = pagination.items

        # 把页面对象变成数组，用数组作为数据源
        data = []
        num = 0
        for obj in objs:
            num = num + 1
            objSearchValue(num, search_value, data, obj)
        res = {
            # 看文档 这四个都是必要的参数，还有个error可传可不传
            'draw': draw,
            'recordsTotal': recordsTotal,
            'recordsFiltered': recordsFiltered,
            'data': data,
            'search_value': search_value
        }
        # log(jsonify(res))
        return jsonify(res)


@datamanage.route('/landSellSearchTableAdder01', methods=['GET', 'POST'])
@limiter.limit("2/second", error_message="OverSpeed",
               exempt_when=lambda: len(str(request.get_json("search_value").get("search_value"))) != 0)
def landSellSearchTableAdder01():
    column_order = ["FID",
                    "REGION_NAME",
                    "NOTICE_NUM",
                    "LAND_LOCATION",
                    "TOTAL_AREA",
                    "CONSTRUCTION_AREA",
                    "PLAN_BUILD_AREA",
                    # "USE_NAME",
                    "PLAN_USE_CUSTOM",
                    "FLOOR_AREA_RATIO",
                    "GREENING_RATE",
                    "BUSSINESS_PROPORTION",
                    "BUILDING_DENSITY",
                    "ASSIGNMENT_METHOD",
                    "ASSIGNMENT_LIMIT",
                    "DATE_BEGIN",
                    "DATE_END",
                    "PRICE_BEGIN",
                    "SECURITY_DEPOSIT",
                    "NOTICE_USE"
                    ]
    if request.method == 'POST':
        land_search_data = json.loads(request.get_data())
        # log("land_search_data:", land_search_data)
        draw = land_search_data['draw']
        start = land_search_data['start']
        length = land_search_data['length']
        page = land_search_data['page']
        s_day = land_search_data['s_day']
        search_value = land_search_data['search_value']
        if s_day == '':
            s_day = '1900-01-01'
        else:
            mon = s_day[0:2]
            day = s_day[3:5]
            year = s_day[6:10]
            s_day = year + '-' + mon + '-' + day
        e_day = land_search_data['e_day']
        if e_day == '':
            e_day = '2300-01-01'
        else:
            mon = e_day[0:2]
            day = e_day[3:5]
            year = e_day[6:10]
            e_day = year + '-' + mon + '-' + day
        # log(e_day, s_day)
        region_name_list = [w.REGION_CODE for w in DICT_REGION.query.filter(
            DICT_REGION.REGION_NAME.in_(land_search_data['region_name_list'])).all()]
        land_location = '%' + land_search_data['land_location'] + '%'
        assignment_method_list = land_search_data['assignment_method_list']  # 出让方式
        assignment_limit_list = land_search_data['assignment_limit_list']  # 出让年限
        # plan_use_list = [w.USE_CODE for w in DICT_LAND_USE.query.filter(
        #     DICT_LAND_USE.USE_NAME.in_(land_search_data['plan_use_list'])).all()]  # 用途分类
        plan_use_list = land_search_data['plan_use_list']
        order = land_search_data['order']  # 排序方式

        # 查询条件定义
        # 行政区+公告时间+土地坐落
        if region_name_list == [] or str(region_name_list).__contains__('全部'):
            region_rules = and_(*[LAND_SELL_INFO.REGION_CODE.like(w) for w in ['%']],
                                LAND_SELL_INFO.LAND_LOCATION.like(land_location), LAND_SELL_INFO.DATE_BEGIN >= s_day,
                                LAND_SELL_INFO.DATE_END <= e_day)
        else:
            region_rules = and_(*[LAND_SELL_INFO.REGION_CODE.in_(w) for w in [region_name_list]],
                                LAND_SELL_INFO.LAND_LOCATION.like(land_location), LAND_SELL_INFO.DATE_BEGIN >= s_day,
                                LAND_SELL_INFO.DATE_END <= e_day)

        # 出让方式
        if assignment_method_list == [] or str(assignment_method_list).__contains__('全部'):
            assignment_method_rules = and_(*[LAND_SELL_INFO.ASSIGNMENT_METHOD.like(w) for w in ['%']])
        else:
            assignment_method_rules = and_(*[LAND_SELL_INFO.ASSIGNMENT_METHOD.in_(w) for w in [assignment_method_list]])

        # 出让年限
        if assignment_limit_list == [] or str(assignment_limit_list).__contains__('全部'):
            assignment_limit_rules = and_(*[LAND_SELL_INFO.ASSIGNMENT_LIMIT.like(w) for w in ['%']])
        else:
            assignment_limit_rules = and_(*[LAND_SELL_INFO.ASSIGNMENT_LIMIT.in_(w) for w in [assignment_limit_list]])

        # 用途分类
        if plan_use_list == [] or str(assignment_limit_list).__contains__('全部'):
            plan_use_rules = and_(*[LAND_SELL_INFO.PLAN_USE.like(w) for w in ['%']])
        else:
            plan_use_rules = and_(*[LAND_SELL_INFO.PLAN_USE_CUSTOM.in_(w) for w in [plan_use_list]])

        if (order[0].get('dir') == 'desc'):  # 确定排序方法
            recordsFiltered = LAND_SELL_INFO.query \
                .filter(region_rules,
                        assignment_method_rules,
                        assignment_limit_rules,
                        plan_use_rules).count()  # 记录数
            # 这边用paginate来获取请求页码的数据
            pagination = LAND_SELL_INFO.query \
                .join(DICT_REGION,
                      LAND_SELL_INFO.REGION_CODE == DICT_REGION.REGION_CODE) \
                .join(DICT_LAND_USE,
                      LAND_SELL_INFO.PLAN_USE_CUSTOM == DICT_LAND_USE.USE_CODE
                      ) \
                .with_entities(
                LAND_SELL_INFO.FID,
                LAND_SELL_INFO.NOTICE_NUM,
                LAND_SELL_INFO.LAND_LOCATION,
                LAND_SELL_INFO.TOTAL_AREA,
                LAND_SELL_INFO.CONSTRUCTION_AREA,
                LAND_SELL_INFO.PLAN_BUILD_AREA,
                LAND_SELL_INFO.NOTICE_USE,
                DICT_LAND_USE.USE_NAME,
                LAND_SELL_INFO.PLAN_USE_CUSTOM,
                LAND_SELL_INFO.FLOOR_AREA_RATIO,
                LAND_SELL_INFO.GREENING_RATE,
                LAND_SELL_INFO.BUSSINESS_PROPORTION,
                LAND_SELL_INFO.BUILDING_DENSITY,
                LAND_SELL_INFO.ASSIGNMENT_METHOD,
                LAND_SELL_INFO.ASSIGNMENT_LIMIT,
                LAND_SELL_INFO.DATE_BEGIN,
                LAND_SELL_INFO.DATE_END,
                DICT_REGION.REGION_NAME,
                LAND_SELL_INFO.PRICE_BEGIN,
                LAND_SELL_INFO.SECURITY_DEPOSIT,
                LAND_SELL_INFO.CREATE_BY,
                LAND_SELL_INFO.CREATE_TIME,
                LAND_SELL_INFO.MODIFIER_BY,
                LAND_SELL_INFO.MODIFIER_TIME
            ).filter(region_rules,
                     assignment_method_rules,
                     assignment_limit_rules,
                     plan_use_rules) \
                .order_by(desc(column_order[order[0].get('column')])) \
                .paginate(page=page, per_page=length, error_out=True)
        else:
            recordsFiltered = LAND_SELL_INFO.query \
                .filter(region_rules,
                        assignment_method_rules,
                        assignment_limit_rules,
                        plan_use_rules).count()  # 记录数
            # 这边用paginate来获取请求页码的数据
            pagination = LAND_SELL_INFO.query \
                .join(DICT_REGION,
                      LAND_SELL_INFO.REGION_CODE == DICT_REGION.REGION_CODE) \
                .join(DICT_LAND_USE,
                      LAND_SELL_INFO.PLAN_USE_CUSTOM == DICT_LAND_USE.USE_CODE
                      ) \
                .with_entities(
                LAND_SELL_INFO.FID,
                LAND_SELL_INFO.NOTICE_NUM,
                LAND_SELL_INFO.LAND_LOCATION,
                LAND_SELL_INFO.TOTAL_AREA,
                LAND_SELL_INFO.CONSTRUCTION_AREA,
                LAND_SELL_INFO.PLAN_BUILD_AREA,
                LAND_SELL_INFO.NOTICE_USE,
                DICT_LAND_USE.USE_NAME,
                LAND_SELL_INFO.PLAN_USE_CUSTOM,
                LAND_SELL_INFO.FLOOR_AREA_RATIO,
                LAND_SELL_INFO.GREENING_RATE,
                LAND_SELL_INFO.BUSSINESS_PROPORTION,
                LAND_SELL_INFO.BUILDING_DENSITY,
                LAND_SELL_INFO.ASSIGNMENT_METHOD,
                LAND_SELL_INFO.ASSIGNMENT_LIMIT,
                LAND_SELL_INFO.DATE_BEGIN,
                LAND_SELL_INFO.DATE_END,
                DICT_REGION.REGION_NAME,
                LAND_SELL_INFO.PRICE_BEGIN,
                LAND_SELL_INFO.SECURITY_DEPOSIT,
                LAND_SELL_INFO.CREATE_BY,
                LAND_SELL_INFO.CREATE_TIME,
                LAND_SELL_INFO.MODIFIER_BY,
                LAND_SELL_INFO.MODIFIER_TIME
            ).filter(region_rules,
                     assignment_method_rules,
                     assignment_limit_rules,
                     plan_use_rules) \
                .order_by(asc(column_order[order[0].get('column')])) \
                .paginate(page=page, per_page=length, error_out=True)

        recordsTotal = recordsFiltered
        objs = pagination.items

        # 把页面对象变成数组，用数组作为数据源
        data = []
        num = 0
        for obj in objs:
            num = num + 1
            objSearchValue(num, search_value, data, obj)
        res = {
            # 看文档 这四个都是必要的参数，还有个error可传可不传
            'draw': draw,
            'recordsTotal': recordsTotal,
            'recordsFiltered': recordsFiltered,
            'data': data,
            'search_value': search_value
        }
        # log(jsonify(res))
        return jsonify(res)
