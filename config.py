DEBUG = True

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

THREADS_PER_PAGE = 2

CSRF_ENABLED = True

DATABASE = 'flask_demo.db'

CSRF_SESSION_KEY = 'secret'

SECRET_KEY = 'secret'

TEMPLATES_AUTO_RELOAD = True