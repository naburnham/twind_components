from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix = "/home")

@bp.route('/table')
def index():
    return render_template('index/table.html')
