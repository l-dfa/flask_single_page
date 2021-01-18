# :filename: single_page/oneel/views.py        this is the views module

# std libs import

# 3rd parties libs import
from flask import Blueprint, render_template

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
