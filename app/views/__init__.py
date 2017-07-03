from flask import Blueprint

main_bp = Blueprint('main_bp', __name__)
admin_bp = Blueprint('admin_bp', __name__)
home_bp = Blueprint('home_bp', __name__)

from . import main, admin, home