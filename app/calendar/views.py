import uuid

from app.models import USER_CALENDAR
from . import calendar
from flask import render_template, request
from flask_login import login_required
import json
from app import db
from app.util import log, comments

from random import randrange
from pyecharts import options as opts
from pyecharts.charts import Bar,Geo
from pyecharts.faker import Collector, Faker
from pyecharts.globals import ChartType, SymbolType


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
    log(comments(USER_CALENDAR, UID))
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
    log(id, TITLE, START, END, UID, URL)
    UC = USER_CALENDAR(id=ID, UID=UID, TITLE=TITLE, START=START, END=END, URL=URL)
    db.session.add(UC)
    db.session.commit()
    # log(id, TITLE, START, END, UID)
    return_dict = {'return_code': '200', 'return_info': '', 'result': False}
    return json.dumps(return_dict, ensure_ascii=False)


# 以下为ly作测试使用
C = Collector()
@C.funcs
def geo_lines() -> Geo:
    c = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "",
            [("广州", 55), ("北京", 66), ("杭州", 77), ("重庆", 88)],
            type_=ChartType.EFFECT_SCATTER,
            color="white",
        )
        .add(
            "geo",
            [("广州", "上海"), ("广州", "北京"), ("广州", "杭州"), ("广州", "重庆")],
            type_=ChartType.LINES,
            effect_opts=opts.EffectOpts(
                symbol=SymbolType.ARROW, symbol_size=6, color="blue"
            ),
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Geo-Lines"))
    )
    return c

@calendar.route('/test')
@login_required
def calendarHome():
    return render_template('calendar/calendar_ly.html')


@calendar.route("/barChart")
def get_bar_chart():
    c = geo_lines()
    return c.dump_options_with_quotes()