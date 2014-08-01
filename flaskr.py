import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

#The Config object works similar to a dictionary
#so we can update it with new values.
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, "flaskr.db"),
    DEBUG=True,
    SECRET_KEY="birth:901120",
    USERNAME="Seulkiming",
    PASSWORD="default"))
app.config.from_envvar("FLASKR_SETTINGS", silent=True)


def connect_db():
    rv = sqlite3.connect(app.config["DATABASE"])
    rv.row_factory = sqlite3.Row
    return rv

if __name__ == "__main__":
    app.run()
