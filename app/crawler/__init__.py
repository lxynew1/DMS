from flask import Blueprint

crawler = Blueprint('crawler', __name__)

from . import views