from . import calendar
from flask import render_template


@calendar.route('/')
def calendar():
    return render_template('calendar/calendar.html')
