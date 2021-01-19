flask_single_page
=====================

This **minimal** Flask project shows a simple
page in two different versions:

* single language;
* two languages.

Needed knowledges
-------------------

This is not a training *ab initio*. It's a fast note just to remember
how to do it. So, to understand this note you need to know:

* what is a web site, a programming language, a development framework;
* a basic knowledge of Python, html, http;
* what is a virtual environment about Python;
* console commands in the operating system of your development personal computer;
* how works a template system, specifically `Jinja <https://jinja.palletsprojects.com/en/2.11.x/>`_.

Methodology
--------------

To make our project, we are going to use Flask's `blueprint(s) <https://flask.palletsprojects.com/en/1.1.x/tutorial/views/>`_: one blueprint to
show the single language html page. The other to show the double
languages html page.

Each blueprint is an app, and our site (an application) will be formed by these
two apps.

Prerequisites of the development environment
---------------------------------------------

Base environments:

* `git <https://git-scm.com/downloads>`_
* `python <https://www.python.org/downloads/>`_ >= 3.8

No third parties libraries.

To install the development environment and run it
----------------------------------------------------

In cmd::

    >git clone https://github.com/l-dfa/flask_single_page.git
    >cd flask_single_page
    >python -m venv venv                     # install python's virtual environment in flask_single_page/venv ...
    >venv\Scripts\activate                   # ... and activate it
    (venv) >python -m pip install -U pip     # upgrade pip
    (venv) >pip install flask                # install flask in virtual env.
    (venv) >pip install Flask-Babel          # install flask-babel in virtual env.
    (venv) >python run.py
  
More infos
------------

@ these links:

* `Flask: how show a page with single language <https://luciano.defalcoalfano.it/blog/show/how_create_minimal_flask_project>`_;
* `Flask: how show a page with two languages <https://luciano.defalcoalfano.it/blog/show/how_create_minimal_flask_project_2nd_part>`_;
* `Flask: managing the URLs <https://luciano.defalcoalfano.it/blog/show/how_create_minimal_flask_project_3rd_part>`_.

License
----------

`CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`_
