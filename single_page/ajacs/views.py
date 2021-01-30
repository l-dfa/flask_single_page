# :filename: single_page/ajacs/views.py        this is the views module

# std libs import
from datetime import datetime

# 3rd parties libs import
from flask import (Blueprint,
                   jsonify,
                   render_template, 
                   current_app, 
                   request)

# project modules import
from single_page import sitemap
from single_page.ajacs import models

# this app will respond to srv/aj/... URLs
ajacs = Blueprint('ajacs', 
                  __name__, 
                  static_folder='static',
                  template_folder='templates', 
                  url_prefix='/ajacs')

@ajacs.route('/_get_nation_data', methods=['POST',])
def get_nation_data():
    code = request.json
    data = models.NationData.get(code)
    return jsonify(data)


@ajacs.route('/')                 # index URLs
def index():
    current_app.logger.debug('> index')
    nations = models.Nations
    return render_template('ajindex.html',
                           title='ajax page title',
                           nations=nations,
                           )


@sitemap.register_generator
def index():
    '''generate URLs using language codes
    
       Note. used by flask-sitemap
    '''
    yield 'ajacs.index', {}, datetime.now(), 'monthly', 0.7