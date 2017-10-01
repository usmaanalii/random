import os
import sqlite3
from flask import (
    Flask,
    request,
    session,
    g,
    redirect,
    url_for, abort,
    render_template,
    flash
)

app = Flask(__name__)
app.config.from_object(__name__)  # Load config from flaskr.py

# Load default config and ovveride config from env variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)
