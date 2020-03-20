import json

from flask import render_template, request
from flask_login import login_required

from . import wechat
# from .forms import LoginForm
from ..models import DICT_REGION, LAND_SELL_INFO
from ..global_fun import maxDate,allDay


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
        return json.dumps(return_dict, ensure_ascii=False)  # ensure_ascii=False才能输出中文
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
    result_end  = LAND_SELL_INFO.query.join(DICT_REGION,
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

    all_day_list=allDay(year)
    for i in all_day_list:
        if i not in land_info_dict:
            land_info_dict[i] = {'tag':'abcd'}
    print(land_info_dict)
    temp_land_info_dict=sorted(land_info_dict.items(), key=lambda x: x[0])
    final_land_info_dict = {}
    for i in temp_land_info_dict:
        print(i)
        final_land_info_dict[i[0]]=i[1]

    return_dict['return_info'] = final_land_info_dict

    return json.dumps(return_dict, ensure_ascii=False)
