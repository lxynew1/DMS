from app.models import USER_CALENDAR, comments
from . import calendar
from flask import render_template, request, jsonify
from flask_login import login_required
import json
from app import db


@calendar.route('/')
@login_required
def calendar_home():
    return render_template('calendar/calendar.html')


@calendar.route('/get_user_json', methods=['GET', 'POST'])
def get_user_json():
    return_dict = {"return_info": '', 'return_code': '200'}
    if request.args is None:
        return_dict['return_code'] = '50004'
        return_dict['return_info'] = '传入参数为空'
        return json.dumps(return_dict, ensure_ascii=False)  # ensure_ascii=False才能输出中文
    # 获取传入的参数
    GET_UID = request.args.to_dict()
    UID = GET_UID.get('UID')
    # 对参数进行操作
    # CALENDARS = USER_CALENDAR.query.filter_by(UID=UID).all()
    print(comments(USER_CALENDAR, UID))
    return_dict['return_info'] = comments(USER_CALENDAR, UID)
    return json.dumps(return_dict, ensure_ascii=False)
