from flask import Blueprint

api = Blueprint("api", __name__)

from . import api_ver_1_0
