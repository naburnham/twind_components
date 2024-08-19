from flask import Blueprint, render_template
from .sample_json_64kb import sample_data

bp = Blueprint('components', __name__, url_prefix = "/component")

@bp.route('/table')
def table():
    return render_template('components/table.html', data=sample_data)

@bp.route('/pagination')
def pagination():
    max_pages: int = 8
    return render_template('components/pagination.html', max_pages=max_pages)

@bp.route('/spinner')
def spinner():
    return render_template('components/spinner.html')
