#!/usr/bin/env python3
"""
Create a get_locale function with the babel.localeselector decorator
"""
import pytz
from flask import Flask, request, render_template, g
from flask_babel import Babel
from typing import Dict, Union


class Config:
    """
    Configure available languages["en", "fr"]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Returns a user dictionary or None if the ID cannot be found or if
    login_as was not passed
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Uses get_user to find a user if any, and set it as a global on flask.g.user
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    Uses a user’s preferred local if it is supported
    """
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """Retrieves the timezone for a web page.
    """
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    """
    Return render template index.html
    """
    g.time = format_datetime()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
