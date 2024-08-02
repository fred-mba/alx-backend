#!/usr/bin/env python3
"""
Create a get_locale function with the babel.localeselector decorator
"""
from flask import Flask, request, render_template
from flask_babel import Babel

LANGUAGES = ["en", "fr"]
BABEL_DEFAULT_LOCALE = "en"
BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)

@app.route('/')
def index() -> str:
    """
    Return render template 2-index.html
    """
    return render_template('2-index.html')

def get_locale():
    """
    The fuction looks at user request and pick the best language translation
    to use for that request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)