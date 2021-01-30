# :filename: single_page/__init__.py

# std libs import
import os
import logging
from   logging.handlers import RotatingFileHandler

# 3rd parties libs import
from flask import Flask
from flask_babel   import Babel
from flask_sitemap import Sitemap

babel = Babel()
sitemap = Sitemap()

def create_app(test=False):
    '''create and configure the app'''
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)

    set_config(app)
    if not test:
        set_logger(app)

    from .oneel import views as views1
    app.register_blueprint(views1.oneel)

    from .twoels import views as views2
    app.register_blueprint(views2.twoels)

    from .ajacs import views as views3
    app.register_blueprint(views3.ajacs)

    babel.init_app(app)
    sitemap.init_app(app)

    @app.route('/sitemap')
    def ep_sitemap():                            # endpoint for sitemap
        return sitemap.sitemap(), 200, {'Content-Type': 'text/xml', }
    
    return app

def set_config(app):
    '''setting configuration '''
    app.config.from_mapping(
        SECRET_KEY='leave-hope-to-enter',
        LANGUAGES = {'en': 'english', 'it': 'italiano',},
        LOG = {
                'DIR' : os.path.join(app.instance_path, 'logs'),
                'FILE': os.path.join(app.instance_path, 'logs/covid.log'),
                'BUFSIZE': 102400,
                'FILE_HANDLER_LEVEL': logging.DEBUG,
                'APP_LOGGER_LEVEL'  : logging.DEBUG,
              }
    )

def set_logger(app):
    '''setting logger'''
    # ensure the log folder exists
    if not os.path.exists(app.config['LOG']['DIR']):
        os.mkdir(app.config['LOG']['DIR'])
    file_handler = RotatingFileHandler(app.config['LOG']['FILE'], maxBytes=app.config['LOG']['BUFSIZE'],
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(app.config['LOG']['FILE_HANDLER_LEVEL'])
    app.logger.addHandler(file_handler)
    
    app.logger.setLevel(app.config['LOG']['APP_LOGGER_LEVEL'])
    app.logger.debug('Covid application starts')
