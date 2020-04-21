import json

from flask import render_template, request
from flask_login import login_required
from sqlalchemy import and_, func
from collections import defaultdict

from . import tools
from ..global_fun import allDay, allRegion
# from .forms import LoginForm
from ..models import DICT_REGION, LAND_SELL_INFO

@login_required
@tools.route('/word2pdf')
def word2Pdf():
    return render_template('tools/word2pdf.html')

