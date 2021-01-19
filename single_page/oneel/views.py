# :filename: single_page/oneel/views.py        this is the views module

# std libs import
from datetime import datetime

# 3rd parties libs import
from flask import Blueprint, render_template

# project modules import
from single_page import sitemap

# this app will respond to srv/1l/... URLs
oneel = Blueprint('oneel', 
                  __name__, 
                  static_folder='static',
                  template_folder='templates', 
                  url_prefix='/1l')

@oneel.route('/')                 # index URLs
@oneel.route('/index')
@oneel.route('/index.html')
def index():
    return render_template('index.html', title='single language title')


@sitemap.register_generator
def index():
    '''generate URLs using language codes
    
       Note. used by flask-sitemap
    '''
    yield 'oneel.index', {}, datetime.now(), 'monthly', 0.7