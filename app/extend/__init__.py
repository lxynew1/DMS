from flask import Blueprint

extend = Blueprint('extend', __name__)

from . import report_generate