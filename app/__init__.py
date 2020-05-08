from flask import Flask, render_template, url_for, redirect
from . import db
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_object('config')
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)

    from app.mod_pages.controllers import mod_pages as page_modules
    from app.mod_pages.home_controller import home_pages
    from app.mod_pages.auth import bp as auth_pages
    from app.mod_pages.blog import bp as blog_pages

    # app.register_blueprint(page_modules)
    # app.register_blueprint(home_pages)
    app.register_blueprint(auth_pages)
    app.register_blueprint(blog_pages)
    app.add_url_rule('/', endpoint='index')

    # @app.errorhandler(404)
    # def not_found(error):
    #     return render_template('404.html')
    return app
