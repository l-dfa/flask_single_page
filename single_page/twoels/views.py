# :filename: single_page/twoels/views.py        this is the views module

# std libs import
from datetime import datetime

# 3rd parties libs import
from flask import Blueprint, current_app, render_template, request, g
from flask_babel import _

# project modules import
from single_page import babel
from single_page import sitemap

# this app will respond to srv/<lang_code>/2l/... URLs
twoels = Blueprint('twoels', 
                   __name__, 
                   static_folder='static',
                   template_folder='templates', 
                   url_prefix='/<lang_code>/2l')

@twoels.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

@twoels.url_value_preprocessor
def pull_lang_code(endpoint, values):
    lc = values.get('lang_code', None)
    if lc in current_app.config['LANGUAGES']:
        g.lang_code = values.pop('lang_code')                # we'll use this even to set request.accept_languages
    else:
        raise ValueError(f"language {lc} is not accepted, because not in {tuple(current_app.config['LANGUAGES'].keys())}")

@twoels.route('/')                 # index URLs
@twoels.route('/index')
@twoels.route('/index.html')
def index():
    # default language code is in babel.default_locale
    current_app.logger.debug('> index')
    return render_template('2lindex.html', title=_('two languages title'))

@babel.localeselector
def get_locale():
    #<! to test Italian language: configure web browser OR ...
    #   ... decomment the following line of code 
    #return 'it'
    if g.get('lang_code', None):
        return request.accept_languages.best_match([g.lang_code,])
    return request.accept_languages.best_match(current_app.config['LANGUAGES'].keys())
    
@sitemap.register_generator
def index():
    '''generate URLs using language codes
    
       Note. used by flask-sitemap
    '''
    for lc in current_app.config['LANGUAGES'].keys():
        g.lang_code = lc                               # used by add_language_code
        #yield 'twoels.index', {'lang_code': lc}
        yield 'twoels.index', {}, datetime.now(), 'monthly', 0.7
