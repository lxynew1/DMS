import json

from flask import render_template, request
from flask_login import login_required

from . import wechat
from ..global_fun import allDay
# from .forms import LoginForm
from ..models import DICT_REGION, LAND_SELL_INFO


@wechat.route('/index')
def index():
    return render_template('wechat/index.html')


@login_required
@wechat.route('/api/calendar/data')
def calendarData():
    return_dict = {'return_code': '200', 'return_info': '', 'result_begin': True}
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'
    else:
        get_data = request.args.to_dict()
        year = get_data.get('year')
        month = get_data.get('month').zfill(2)
        year_month = '{0}-{1}'.format(year, month)
        print(year_month)
        # 查询公告日期
        result_begin = LAND_SELL_INFO.query.join(DICT_REGION,
                                                 LAND_SELL_INFO.REGION_CODE == DICT_REGION.REGION_CODE).with_entities(
            LAND_SELL_INFO.DATE_BEGIN,
            LAND_SELL_INFO.DATE_END,
            DICT_REGION.REGION_NAME,
            DICT_REGION.TYPE,
            LAND_SELL_INFO.NOTICE_NUM).filter(
            LAND_SELL_INFO.DATE_BEGIN.like("%" + year_month + "%")).all()
        land_info_dict = {}
        for i in result_begin:
            detail_dict_begin = {}
            if i.DATE_BEGIN in land_info_dict:
                tag_value = land_info_dict[i.DATE_BEGIN]["tag"]
            else:
                tag_value = 'abcd'

            # 四位标识码，依次表示主城区公告、主城区成交、区县公告、区县成交
            if i.TYPE == '1':
                detail_dict_begin['tag'] = tag_value.replace('a', 'A')
            else:
                detail_dict_begin['tag'] = tag_value.replace('c', 'C')

            land_info_dict[i.DATE_BEGIN] = detail_dict_begin

        # 查询成交日期
        result_end = LAND_SELL_INFO.query.join(DICT_REGION,
                                               LAND_SELL_INFO.REGION_CODE == DICT_REGION.REGION_CODE).with_entities(
            LAND_SELL_INFO.DATE_BEGIN,
            LAND_SELL_INFO.DATE_END,
            DICT_REGION.REGION_NAME,
            DICT_REGION.TYPE,
            LAND_SELL_INFO.NOTICE_NUM).filter(
            LAND_SELL_INFO.DATE_END.like("%" + year_month + "%")).all()
        for i in result_end:
            detail_dict_end = {}
            if i.DATE_END in land_info_dict:
                tag_value = land_info_dict[i.DATE_END]["tag"]
            else:
                tag_value = 'abcd'

            # 四位标识码，依次表示主城区公告、主城区成交、区县公告、区县成交
            if i.TYPE == '1':
                detail_dict_end['tag'] = tag_value.replace('b', 'B')
            else:
                detail_dict_end['tag'] = tag_value.replace('d', 'D')

            land_info_dict[i.DATE_END] = detail_dict_end

        all_day_list = allDay(year)
        for i in all_day_list:
            if i not in land_info_dict:
                land_info_dict[i] = {'tag': 'abcd'}
        print(land_info_dict)
        temp_land_info_dict = sorted(land_info_dict.items(), key=lambda x: x[0])
        final_land_info_dict = {}
        for i in temp_land_info_dict:
            print(i)
            final_land_info_dict[i[0]] = i[1]

        return_dict['return_info'] = final_land_info_dict

    return json.dumps(return_dict, ensure_ascii=False)


@wechat.route('/api/notice_deal_detail')
def noticeDealDetail():
    return_dict = {'return_code': '200', 'return_info': '', 'result_begin': True}
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'
    else:
        get_data = request.args.to_dict()
        temp_date = get_data.get("date")
        date = temp_date[0,4]+temp_date[4,6]+temp_date[6,8]
        print(date)
        begin_list = []
        result_begin = LAND_SELL_INFO.query.join(DICT_REGION,
                                                 LAND_SELL_INFO.REGION_CODE == DICT_REGION.REGION_CODE).with_entities(
            LAND_SELL_INFO.NOTICE_NUM,
            LAND_SELL_INFO.LAND_LOCATION,
            LAND_SELL_INFO.TOTAL_AREA,
            LAND_SELL_INFO.PLAN_BUILD_AREA,
            LAND_SELL_INFO.PLAN_USE,
            LAND_SELL_INFO.DATE_BEGIN,
            LAND_SELL_INFO.DATE_END,
            DICT_REGION.REGION_NAME,
            LAND_SELL_INFO.NOTICE_NUM).filter(
            LAND_SELL_INFO.DATE_BEGIN.like("" + date + "")).all()
        for i in result_begin:
            notice_dict = {}
            notice_dict["notice_num"] = i.NOTICE_NUM
            notice_dict["land_location"] = i.LAND_LOCATION
            notice_dict["total_area"] = i.TOTAL_AREA
            notice_dict["plan_build_area"] = i.PLAN_BUILD_AREA
            notice_dict["plan_use"] = i.PLAN_USE
            notice_dict["date_begin"] = i.DATE_BEGIN
            notice_dict["date_end"] = i.DATE_END
            notice_dict["region_name"] = i.REGION_NAME
            begin_list.append(notice_dict)

        deal_list=[]
        result_deal = LAND_SELL_INFO.query.join(DICT_REGION,
                                                 LAND_SELL_INFO.REGION_CODE == DICT_REGION.REGION_CODE).with_entities(
            LAND_SELL_INFO.NOTICE_NUM,
            LAND_SELL_INFO.LAND_LOCATION,
            LAND_SELL_INFO.TOTAL_AREA,
            LAND_SELL_INFO.PLAN_BUILD_AREA,
            LAND_SELL_INFO.PLAN_USE,
            LAND_SELL_INFO.DATE_BEGIN,
            LAND_SELL_INFO.DATE_END,
            DICT_REGION.REGION_NAME,
            LAND_SELL_INFO.NOTICE_NUM).filter(
            LAND_SELL_INFO.DATE_END.like("%" + date + "%")).all()
        for i in result_deal:
            notice_dict = {}
            notice_dict["notice_num"] = i.NOTICE_NUM
            notice_dict["land_location"] = i.LAND_LOCATION
            notice_dict["total_area"] = i.TOTAL_AREA
            notice_dict["plan_build_area"] = i.PLAN_BUILD_AREA
            notice_dict["plan_use"] = i.PLAN_USE
            notice_dict["date_begin"] = i.DATE_BEGIN
            notice_dict["date_end"] = i.DATE_END
            notice_dict["region_name"] = i.REGION_NAME
            deal_list.append(notice_dict)
        all_dict = {'notice':begin_list,'deal':deal_list}
        print(all_dict)
    return_dict['return_info'] = all_dict

    return json.dumps(return_dict, ensure_ascii=False)