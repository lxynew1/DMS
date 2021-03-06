import datetime
import json
from uuid import uuid1

from flask import render_template, request
from flask_login import login_required, current_user

from app import db
from . import datamanage
from ..models import DICT_REGION, DICT_LAND_USE, LAND_SELL_INFO, LAND_PARCEL_DETAIL, GEO_PARCEL


# 土拍公告录入界面
@datamanage.route('/land_sell_adder')
@login_required
def landSellAdder():
    db.create_all()
    # 添加分区信息
    r_region = DICT_REGION.query.filter(DICT_REGION.TYPE != '0').all()
    region_dict = {}
    for i in r_region:
        region_dict[i.REGION_CODE] = i.REGION_NAME

    # 添加自定义统计用途分类
    r_custom_use = DICT_LAND_USE.query.filter(DICT_LAND_USE.GRADE == 'CUSTOM_USE_1').all()
    custom_use_dict = {}
    for i in r_custom_use:
        custom_use_dict[i.USE_CODE] = i.USE_NAME

    # 添加标准用途分类信息
    r_standard_use = DICT_LAND_USE.query.filter(DICT_LAND_USE.GRADE == 'CONSTRUCTION_USE_2').all()
    standard_use_dict = {}
    for i in r_standard_use:
        standard_use_dict[i.USE_CODE] = i.USE_CODE + i.USE_NAME

    # 添加自定义分类用途

    return render_template('dataManage/land_sell_adder.html',
                           region_dict=region_dict,
                           custom_use_dict=custom_use_dict,
                           standard_use_dict=standard_use_dict)


# api校验公告编号是否重复
@datamanage.route('/api/notice_no/is_repetition')
def noticeNoIsRepetition():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '', 'result': True}
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'
        return json.dumps(return_dict, ensure_ascii=False)  # ensure_ascii=False才能输出中文
    # 获取传入的参数
    get_data = request.args.to_dict()
    notice_no = get_data.get("notice_no")
    if LAND_SELL_INFO.query.filter(LAND_SELL_INFO.NOTICE_NUM == notice_no).count() >= 1:
        return_dict['return_code'] = '1000'
        return_dict['return_info'] = '公告编号重复，请检查后输入！'
        return_dict['result'] = False
    return json.dumps(return_dict, ensure_ascii=False)


# 处理时间格式
def reformatDate(date_str):
    date_list = date_str.split('/')
    return date_list[-1] + '-' + date_list[0] + '-' + date_list[1]


# 保存土地拍卖信息
@datamanage.route('/api/land_sell_adder/save')
def landSellAdderSave():
    return_dict = {'return_code': '200', 'return_info': '', 'result': True}
    # 判定参数为空，给返回值赋值
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'
        return json.dumps(return_dict, ensure_ascii=False)  # ensure_ascii=False才能输出中文
    get_data = request.args.to_dict()
    notice_no = get_data.get("input_notice_no")
    parcel_no = get_data.get("input_parcel_no")
    if LAND_SELL_INFO.query.filter(LAND_SELL_INFO.NOTICE_NUM == notice_no).count() >= 1:
        return_dict['return_code'] = '1000'
        return_dict['return_info'] = '公告编号重复，请检查后输入！'
        return_dict['result'] = False
    elif LAND_PARCEL_DETAIL.query.filter(LAND_PARCEL_DETAIL.PARCEL_NO == parcel_no).count() >= 1:
        return_dict['return_code'] = '1000'
        return_dict['return_info'] = '地块编号重复，请检查后输入！'
        return_dict['result'] = False
    else:
        fid = str(uuid1())
        land_sell_info = LAND_SELL_INFO(
            FID=fid,
            IS_ONE=get_data.get('is_one'),
            NOTICE_NUM=get_data.get('input_notice_no'),
            LAND_LOCATION=get_data.get('input_land_location'),
            TOTAL_AREA=get_data.get('input_total_area'),
            CONSTRUCTION_AREA=get_data.get('input_construction_area'),
            PLAN_BUILD_AREA=get_data.get('input_plan_area'),
            NOTICE_USE=get_data.get('input_notice_use'),
            PLAN_USE=get_data.get('standard_use_code'),
            PLAN_USE_CUSTOM=get_data.get('select_plan_use_custom'),
            FLOOR_AREA_RATIO=get_data.get('input_floor_area_ratio'),
            GREENING_RATE=get_data.get('input_greening_rate'),
            BUSSINESS_PROPORTION=get_data.get('input_business_proportion'),
            BUILDING_DENSITY=get_data.get('input_building_density'),
            ASSIGNMENT_METHOD=get_data.get('select_assignment_method'),
            ASSIGNMENT_LIMIT=get_data.get('input_assignment_limit'),
            DATE_BEGIN=reformatDate(get_data.get('input_date_begin')),
            DATE_END=reformatDate(get_data.get('input_date_end')),
            REGION_CODE=get_data.get('select_region_code'),
            PRICE_BEGIN=get_data.get('input_price_begin'),
            SECURITY_DEPOSIT=get_data.get('input_security_deposit'),
            CREATE_BY=current_user.id,
            CREATE_TIME=datetime.datetime.now().strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                         '%Y-%m-%d %H:%M:%S')
        )
        try:
            # 如果为独立地块，同时同步到地块详情表中
            if get_data.get('is_one') == "1":
                land_parcel_detail = LAND_PARCEL_DETAIL(
                    FID=str(uuid1()),
                    PARENT_FID=fid,
                    PARCEL_NO=get_data.get('input_parcel_no'),
                    TOTAL_AREA=get_data.get('input_total_area'),
                    PLAN_BUILD_AREA=get_data.get('input_plan_area'),
                    PLAN_USE=get_data.get('standard_use_code'),
                    FLOOR_AREA_RATIO=get_data.get('input_floor_area_ratio'),
                    GREENING_RATE=get_data.get('input_greening_rate'),
                    BUILDING_DENSITY=get_data.get('input_building_density'),
                    ASSIGNMENT_LIMIT=get_data.get('input_assignment_limit'),
                    CREATE_BY=current_user.id,
                    CREATE_TIME=datetime.datetime.now().strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                                 '%Y-%m-%d %H:%M:%S')
                )
                db.session.add(land_parcel_detail)
            db.session.add(land_sell_info)
            db.session.commit()
            return_dict['return_info'] = fid
        except Exception as e:
            print(e)
            return_dict['return_code'] = '1000'
            return_dict['return_info'] = str(e)
            return_dict['result'] = False
    return json.dumps(return_dict, ensure_ascii=False)


# 地块录入界面
@login_required
@datamanage.route('/land_parcel_detail')
def landParcelDetail():
    land_sell_info_fid = request.values.get('fid')
    try:
        notice_no = LAND_SELL_INFO.query.filter(LAND_SELL_INFO.FID == land_sell_info_fid).first().NOTICE_NUM
    except:
        notice_no = "无"
    r_parcel_detail = LAND_PARCEL_DETAIL.query.outerjoin(GEO_PARCEL,
                                                    LAND_PARCEL_DETAIL.FID == GEO_PARCEL.PARCEL_FID).with_entities(
        LAND_PARCEL_DETAIL.PARCEL_NO,
        LAND_PARCEL_DETAIL.TOTAL_AREA,
        LAND_PARCEL_DETAIL.PLAN_USE,
        LAND_PARCEL_DETAIL.FID,
        GEO_PARCEL.FID
        ).filter(
        LAND_PARCEL_DETAIL.PARENT_FID == land_sell_info_fid).all()
    parcel_detail_list = []
    for i in r_parcel_detail:
        print(i[0])
        one_parcel_list = [i[0],
                           i[1],
                           i[2],
                           i[3],
                           i[4]]
        parcel_detail_list.append(one_parcel_list)
    print(parcel_detail_list)
    # 标准用途分类
    r_standard_use = DICT_LAND_USE.query.filter(DICT_LAND_USE.GRADE == 'CONSTRUCTION_USE_2').all()
    standard_use_dict = {}
    for i in r_standard_use:
        standard_use_dict[i.USE_CODE] = i.USE_CODE + i.USE_NAME
    # 返回公告编号、地块详情、标准分类到前端显示，公告fid隐藏
    return render_template('dataManage/land_parcel_detail.html',
                           notice_no=notice_no,
                           parcel_detail_list=parcel_detail_list,
                           land_sell_info_fid=land_sell_info_fid,
                           standard_use_dict=standard_use_dict)


# 地块数据保存api
@datamanage.route('/api/land_parcel_detail/save')
def landParcelDetailSave():
    return_dict = {'return_code': '200', 'return_info': '', 'result': True}
    # 判定参数为空，给返回值赋值
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'
        return json.dumps(return_dict, ensure_ascii=False)  # ensure_ascii=False才能输出中文
    get_data = request.args.to_dict()
    parcel_no = get_data.get("input_parcel_no")
    if LAND_PARCEL_DETAIL.query.filter(LAND_PARCEL_DETAIL.PARCEL_NO == parcel_no).count() >= 1:
        return_dict['return_code'] = '1000'
        return_dict['return_info'] = '地块编号重复，请检查后输入！'
        return_dict['result'] = False
    else:
        fid = str(uuid1())
        land_parcel_detail = LAND_PARCEL_DETAIL(
            FID=fid,
            PARENT_FID=get_data.get('input_land_sell_info_fid'),
            PARCEL_NO=get_data.get('input_parcel_no'),
            TOTAL_AREA=get_data.get('input_total_area'),
            PLAN_BUILD_AREA=get_data.get('input_plan_area'),
            PLAN_USE=get_data.get('select_plan_use'),
            FLOOR_AREA_RATIO=get_data.get('input_floor_area_ratio'),
            GREENING_RATE=get_data.get('input_greening_rate'),
            BUILDING_DENSITY=get_data.get('input_building_density'),
            ASSIGNMENT_LIMIT=get_data.get('input_assignment_limit'),
            CREATE_BY=current_user.id,
            CREATE_TIME=datetime.datetime.now().strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                         '%Y-%m-%d %H:%M:%S')
        )
        try:
            db.session.add(land_parcel_detail)
            db.session.commit()
        except Exception as e:
            print(e)
            return_dict['return_code'] = '1000'
            return_dict['return_info'] = str(e)
            return_dict['result'] = False
    return json.dumps(return_dict, ensure_ascii=False)


# 校验地块编号是否重复
@datamanage.route('/api/parcel_no/is_repetition')
def parcelNoIsRepetition():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '', 'result': True}
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'
        return json.dumps(return_dict, ensure_ascii=False)  # ensure_ascii=False才能输出中文
    # 获取传入的参数
    get_data = request.args.to_dict()
    parcel_no = get_data.get("parcel_no")
    if LAND_PARCEL_DETAIL.query.filter(LAND_PARCEL_DETAIL.PARCEL_NO == parcel_no).count() >= 1:
        return_dict['return_code'] = '1000'
        return_dict['return_info'] = '地块编号重复，请检查后输入！'
        return_dict['result'] = False
    return json.dumps(return_dict, ensure_ascii=False)
