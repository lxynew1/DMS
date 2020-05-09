import datetime
import json
from uuid import uuid1

from flask import render_template, request
from flask_login import login_required, current_user

from app import db
from . import datamanage
from ..models import ENTERPISE_INFO, LAND_SELL_DEAL, R_SELLDEAL_ENTERPISE,LAND_SELL_INFO


# 土地成交页面
@login_required
@datamanage.route('/land_sell_deal')
def landSellDeal():

    land_sell_info_fid = request.values.get('fid')
    try:
        notice_no = LAND_SELL_INFO.query.filter(LAND_SELL_INFO.FID == land_sell_info_fid).first().NOTICE_NUM
    except:
        notice_no = "无"
    is_deal = LAND_SELL_DEAL.query.filter(LAND_SELL_DEAL.PARENT_FID == land_sell_info_fid).count()
    land_sell_info_fid_count=LAND_SELL_INFO.query.filter(LAND_SELL_INFO.FID == land_sell_info_fid).count()
    print(is_deal)
    r_enterprise = ENTERPISE_INFO.query.filter().all()
    enterprise_dict = {}
    for i in r_enterprise:
        enterprise_dict[i.FID] = i.NAME

    r_top_enterprise = ENTERPISE_INFO.query.filter(ENTERPISE_INFO.IS_FIRST == "1").all()
    top_enterprise_dict = {}
    for i in r_top_enterprise:
        top_enterprise_dict[i.FID] = i.TOP_LEVEL

    return render_template('dataManage/land_sell_deal.html',
                           land_sell_info_fid=land_sell_info_fid,
                           enterprise_dict=enterprise_dict,
                           top_enterprise_dict=top_enterprise_dict,
                           is_deal=is_deal,
                           land_sell_info_fid_count=land_sell_info_fid_count,
                           notice_no=notice_no)


# 保存成交数据
@datamanage.route('/api/save_land_deal')
def saveLandDeal():
    return_dict = {'return_code': '200', 'return_info': '', 'result': True}
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'
        return json.dumps(return_dict, ensure_ascii=False)  # ensure_ascii=False才能输出中文
    else:
        get_data = request.args.to_dict()
        land_sell_deal_fid = str(uuid1())
        input_land_sell_info_fid = get_data.get("input_land_sell_info_fid")
        state = '0'

        land_sell_deal = LAND_SELL_DEAL(
            FID=land_sell_deal_fid,
            PARENT_FID=input_land_sell_info_fid,
            DEAL_PRICE=get_data.get("input_deal_price"),
            DEAL_ASSIGNMENT_METHOD=get_data.get("select_assignment_method"),
            DATE_DEAL=get_data.get("input_date_deal"),
            CREATE_BY=current_user.id,
            CREATE_TIME=datetime.datetime.now().strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                         '%Y-%m-%d %H:%M:%S')
        )
        try:
            db.session.add(land_sell_deal)
            state = '1'
        except Exception as e:
            print(e)
            return_dict['return_code'] = '1000'
            return_dict['return_info'] = str(e)
            return_dict['result'] = False
            state = '0'
        if state == '1':

            enterprise_fid_list = get_data.get("select_enterprise").split(';')
            if len(enterprise_fid_list)==2:
                enterprise_fid_list.pop()
            else:
                enterprise_fid_list=enterprise_fid_list[:-2]
            for i in range(len(enterprise_fid_list)):
                r_sell_enterprise = R_SELLDEAL_ENTERPISE(
                    FID=str(uuid1()),
                    DEAL_FID=input_land_sell_info_fid,
                    ENTERPISE_FID=enterprise_fid_list[i],
                    CREATE_BY=current_user.id,
                    CREATE_TIME=datetime.datetime.now().strptime(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                                 '%Y-%m-%d %H:%M:%S')
                )
                try:
                    db.session.add(r_sell_enterprise)
                    state = '1'
                except Exception as e:
                    print(e)
                    return_dict['return_code'] = '1000'
                    return_dict['return_info'] = str(e)
                    return_dict['result'] = False
                    state = '0'
                    break
        if state == '0':
            db.session.rollback()
        else:
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                return_dict['return_code'] = '1000'
                return_dict['return_info'] = str(e)
                return_dict['result'] = False

    return json.dumps(return_dict, ensure_ascii=False)
