import uuid

from . import calendar
from flask import render_template, request, jsonify
from flask_login import login_required
import json
from app import db
from ..models import USER_CALENDAR,comments


@calendar.route('/')
@login_required
def calendar_home():
    return render_template('calendar/calendar.html')


@calendar.route('/get_user_json', methods=['GET', 'POST'])
@login_required
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


@calendar.route('/store_user_calendar', methods=['GET', 'POST'])
@login_required
def store_user_calendar():
    DATA = request.args.to_dict()
    ID = str(uuid.uuid4())
    TITLE = str(DATA.get('title'))
    START = str(DATA.get('start'))
    END = str(DATA.get('end'))
    UID = str(DATA.get('UID'))
    URL = str(DATA.get('URL')) if len(str(DATA.get('URL'))) == 0 else '#'
    print(id, TITLE, START, END, UID, URL)
    UC = USER_CALENDAR(id=ID, UID=UID, TITLE=TITLE, START=START, END=END, URL=URL)
    db.session.add(UC)
    db.session.commit()
    print(id, TITLE, START, END, UID)
    return_dict = {'return_code': '200', 'return_info': '', 'result': False}
    return json.dumps(return_dict, ensure_ascii=False)
