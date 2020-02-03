from flask import Blueprint

calendar = Blueprint('calendar', __name__)

from . import views