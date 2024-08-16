from flask import Blueprint, render_template
from .sample_json_64kb import sample_data

bp = Blueprint('home', __name__, url_prefix = "/home")

@bp.route('/table')
def index():
    return render_template('index/table.html', data=sample_data)
