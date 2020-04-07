import datetime
import json
from uuid import uuid1

from flask import request, render_template
from flask_login import current_user, login_required
from sqlalchemy import and_, func

from app import db
from . import wechat
from ..global_fun import center_geolocation
from ..models import DICT_REGION, LAND_SELL_INFO, GEO_PARCEL, LAND_PARCEL_DETAIL


# 高德地图绘制界面
@login_required
@wechat.route('/map/gaode')
def gaoDe():
    parcel_fid = request.values.get('fid')
    return render_template('wechat/gaode.html',
                           parcel_fid=parcel_fid)


# 土交信息首页地图相关值
@wechat.route('/api/map_data_notice')
def mapDataNotice():
    return_dict = {'return_code': '200', 'return_info': '', 'result_begin': True}
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'
    else:
        get_data = request.args.to_dict()
        date_begin = get_data.get("date_begin")
        date_end = get_data.get("date_end")
        result = LAND_SELL_INFO.query.join(DICT_REGION,
                                           LAND_SELL_INFO.REGION_CODE == DICT_REGION.REGION_CODE).with_entities(
            DICT_REGION.REGION_NAME,
            func.sum(LAND_SELL_INFO.TOTAL_AREA),
            func.count(LAND_SELL_INFO.FID),

        ).filter(and_(LAND_SELL_INFO.DATE_BEGIN >= date_begin, LAND_SELL_INFO.DATE_BEGIN <= date_end)
                 ).group_by(DICT_REGION.REGION_NAME).all()

        return_dict['return_info'] = result

    return json.dumps(return_dict, ensure_ascii=False)


# 上传图形数据
@wechat.route('/map/api/post_parcel_geostring', methods=['POST'])
def postParcelGeoString():
    return_dict = {'return_code': '200', 'return_info': '', 'result_begin': True}
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'

    else:
        fid = request.form.get('fid')
        if GEO_PARCEL.query.filter(GEO_PARCEL.PARCEL_FID == fid).count() > 0:
            return_dict['return_code'] = '1000'
            return_dict['return_info'] = '该地块已存在图形'
            return_dict['result'] = False
        else:
            geo_string = request.form.get('geo_string')
            geo_list_temp = geo_string.split(';')
            geo_list = []
            lng_list = []
            lat_list = []
            for i in geo_list_temp:
                tmp_list = i.split(',')
                geo_list.append(tmp_list)
                lng_list.append(tmp_list[0])
                lat_list.append(tmp_list[1])
            geo_parcel = GEO_PARCEL(
                FID=str(uuid1()),
                PARCEL_FID=fid,
                GEO_LIST=str(geo_list),
                GEO_CENTER=str(list(center_geolocation(geo_list))),
                GEO_N=max(lat_list),
                GEO_S=min(lat_list),
                GEO_W=min(lng_list),
                GEO_E=max(lng_list),
                CREATE_BY=current_user.id,
                CREATE_TIME=datetime.datetime.now().strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                             '%Y-%m-%d %H:%M:%S')
            )
            try:
                db.session.add(geo_parcel)
                db.session.commit()
            except Exception as e:
                return_dict['return_code'] = '1000'
                return_dict['return_info'] = str(e)
                return_dict['result'] = False

    return json.dumps(return_dict, ensure_ascii=False)


# 查询界面
@wechat.route('/map/gaode/query')
def gaoDeQuery():
    notice_fid = request.values.get('notice_fid')
    return render_template('wechat/gaode_query.html',
                           notice_fid=notice_fid)


@wechat.route('/map/api/gaode_parcel')
def apiMapGaodeParcel():
    # 以后加入范围参数
    return_dict = {'return_code': '200', 'return_info': '', 'result_begin': True}
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'
    else:
        get_data = request.args.to_dict()
        notice_fid = get_data.get("notice_fid")
        if notice_fid=='' or notice_fid==None:
            notice_fid='1'
        geo_json = {'highlight': '', 'normal': ''}

        result_highlight = GEO_PARCEL.query.join(
            LAND_PARCEL_DETAIL,
            GEO_PARCEL.PARCEL_FID == LAND_PARCEL_DETAIL.FID,
        ).join(
            LAND_SELL_INFO,
            LAND_PARCEL_DETAIL.PARENT_FID == LAND_SELL_INFO.FID
        ).with_entities(
            LAND_SELL_INFO.NOTICE_NUM,
            LAND_PARCEL_DETAIL.PARCEL_NO,
            LAND_PARCEL_DETAIL.PLAN_USE,
            LAND_PARCEL_DETAIL.TOTAL_AREA,
            GEO_PARCEL.GEO_CENTER,
            GEO_PARCEL.GEO_LIST

        ).filter(LAND_SELL_INFO.FID == notice_fid).all()
        result_highlight_list = []
        for i in result_highlight:
            highlight = [
                i[0],
                i[1],
                i[2],
                i[3],
                eval(i[4]),
                eval(i[5]),
            ]
            result_highlight_list.append(highlight)
        geo_json['highlight'] = result_highlight_list

        result_normal = GEO_PARCEL.query.join(
            LAND_PARCEL_DETAIL,
            GEO_PARCEL.PARCEL_FID == LAND_PARCEL_DETAIL.FID,
        ).join(
            LAND_SELL_INFO,
            LAND_PARCEL_DETAIL.PARENT_FID == LAND_SELL_INFO.FID
        ).with_entities(
            LAND_SELL_INFO.NOTICE_NUM,
            LAND_PARCEL_DETAIL.PARCEL_NO,
            LAND_PARCEL_DETAIL.PLAN_USE,
            LAND_PARCEL_DETAIL.TOTAL_AREA,
            GEO_PARCEL.GEO_CENTER,
            GEO_PARCEL.GEO_LIST

        ).filter(LAND_SELL_INFO.FID != notice_fid).all()
        geo_json['normal'] = result_normal
        return_dict['return_info'] = geo_json
    return json.dumps(return_dict, ensure_ascii=False)
