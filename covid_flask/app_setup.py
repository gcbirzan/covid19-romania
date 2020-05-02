import hashlib
import json

from flask import Flask, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

config = {
    'FLASK_ADMIN_SWATCH': 'cerulean',
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SECRET_KEY': 'q²nìd¥S¤&SÍ-Ë',
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300,

}

cache = Cache()


def get_cache_key():
    return hashlib.md5(request.path.encode('utf-8') + request.query_string).hexdigest()


def cache_postprocessor(result, **kwargs):
    cache.set(get_cache_key(), json.dumps(result))
    print('result cached.')


def create_app():
    from .model import Data

    app = Flask(__name__)
    app.config.from_mapping(config)

    db.init_app(app)
    db.app = app
    db.create_all()
    cache.init_app(app)
    admin = Admin(app, name='covid19', template_mode='bootstrap3')

    admin.add_view(ModelView(Data, db.session))

    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    manager = APIManager(app, flask_sqlalchemy_db=db)
    blueprint = manager.create_api_blueprint(Data, app=app, results_per_page=-1, max_results_per_page=-1,
                                             postprocessors={'GET_MANY': [cache_postprocessor]})
    blueprint.after_request(add_cors_headers)

    toolbar = DebugToolbarExtension(app)

    @app.before_request
    def preprocess_request():
        return cache.get(get_cache_key())

    return app
