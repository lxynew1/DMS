from . import calendar
from flask import render_template
from flask_login import login_required


@calendar.route('/')
@login_required
def calendar_home():
    return render_template('calendar/calendar.html')

