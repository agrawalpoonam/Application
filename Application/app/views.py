from app import app
from flask import render_template
from settings import *

@app.route("/registration/")
def render_templates():
    """
    """
    return render_template("registration_page.html")

