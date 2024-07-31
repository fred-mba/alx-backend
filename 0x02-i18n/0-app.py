#!/usr/bin/env python3
"""
Setting up a basic Flask app with a single route that renders
an `index.html` template.
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index() -> str:
    """Return render template `index.html`
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
