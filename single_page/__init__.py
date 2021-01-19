# :filename: single_page/__init__.py

# std libs import

# 3rd parties libs import
from flask import Flask
from flask_babel   import Babel
from flask_sitemap import Sitemap

babel = Babel()
sitemap = Sitemap()

def create_app():
    '''create and configure the app'''
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='leave-hope-to-enter',
        LANGUAGES = {'en': 'english', 'it': 'italiano',},
    )

    from .oneel import views as views1
    app.register_blueprint(views1.oneel)

    from .twoels import views as views2
    app.register_blueprint(views2.twoels)

    babel.init_app(app)
    sitemap.init_app(app)
    
    return app
