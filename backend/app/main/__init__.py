from flask import Blueprint

main = Blueprint("main", __name__)

from . import views  # Blueprints needs to be created before assigning view to them.
