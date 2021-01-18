# :filename: single_page/__init__.py

# std libs import

# 3rd parties libs import
from flask import Flask, current_app, request
from flask_babel import Babel

babel = Babel()

def create_app():
    '''create and configure the app'''
    app = Flask(__name__)
    
    babel.init_app(app)

    app.config.from_mapping(
        SECRET_KEY='leave-hope-to-enter',
        LANGUAGES = {'en': 'english', 'it': 'italiano',},
    )

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from .oneel import views as views1
    app.register_blueprint(views1.oneel)

    from .twoels import views as views2
    app.register_blueprint(views2.twoels)

    return app


@babel.localeselector
def get_locale():
    #<! to test Italian language: configure web browser OR ...
    #   ... decomment the following line of code and comment the final return
    #return 'it'
    return request.accept_languages.best_match(current_app.config['LANGUAGES'].keys())
