# :filename: single_page/twoels/views.py        this is the views module

# std libs import
# import os

# 3rd parties libs import
from flask import Blueprint, render_template

from flask_babel import _
# from flask_babel import lazy_gettext as _l
# from flask_babel import get_locale



# this app will respond to srv/2l/... URLs
twoels = Blueprint('twoels', 
                   __name__, 
                  static_folder='static',
                  template_folder='templates', 
                   url_prefix='/2l')

@twoels.route('/')                 # index URLs
@twoels.route('/index')
@twoels.route('/index.html')
def index():
    return render_template('2lindex.html', title=_('two languages title'))


