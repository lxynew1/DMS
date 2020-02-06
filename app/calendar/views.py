from . import calendar
from flask import render_template
from flask_login import login_required
import json


@calendar.route('/')
@login_required
def calendar_home():
    return render_template('calendar/calendar.html')


@calendar.route('/get_user_json', methods=['GET', 'POST'])
def get_user_json():
    return_dict = {"return_info": [
        {
            "title": "All Day Event",
            "start": "2020-02-06"
        },
        {
            "title": "Long Event",
            "start": "2018-02-07",
            "end": "2020-02-10"
        },
        {
            "id": 999,
            "title": "Repeating Event",
            "start": "2020-02-09T16:00:00"
        },
        {
            "id": 999,
            "title": "Repeating Event",
            "start": "2018-02-16T16:00:00"
        },
        {
            "title": "Conference",
            "start": "2020-02-11",
            "end": "2020-02-13"
        },
        {
            "title": "Meeting",
            "start": "2020-02-12T10:30:00",
            "end": "2020-02-12T12:30:00"
        },
        {
            "title": "Lunch",
            "start": "2018-02-12T12:00:00"
        },
        {
            "title": "Meeting",
            "start": "2020-02-12T14:30:00"
        },
        {
            "title": "Happy Hour",
            "start": "2020-02-12T17:30:00"
        },
        {
            "title": "Dinner",
            "start": "2020-02-12T20:00:00"
        },
        {
            "title": "Birthday Party",
            "start": "2020-02-13T07:00:00"
        },
        {
            "title": "Click for Google",
            "url": "http://google.com/",
            "start": "2020-02-27"
        }
    ]}
    return json.dumps(return_dict, ensure_ascii=False)
