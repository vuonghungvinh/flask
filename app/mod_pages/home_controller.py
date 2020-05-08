from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

home_pages = Blueprint('homepage', __name__)

@home_pages.route('/', defaults={'page': 'index'})
@home_pages.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
