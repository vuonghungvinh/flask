from flask import (Blueprint, flash, render_template, request, session, abort,
                    redirect, url_for)

mod_pages = Blueprint('pages', __name__, url_prefix='/pages')

@mod_pages.route('/hello')
def hello():
    return render_template('pages/hello.html')