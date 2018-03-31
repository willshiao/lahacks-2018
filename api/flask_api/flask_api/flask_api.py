import os 
import sqlite3
import config
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from sqlalchemy import *
from db import *

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('flask_settings', silent=True)

def init_db():
    metadata.create_all()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

def connect_db():
    rv = sqlite3.connect('./test.db')
    rv.row_factory = sqlite3.Row
    return rv

init_db()
