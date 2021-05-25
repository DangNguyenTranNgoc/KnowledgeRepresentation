from flask import (
    Flask,
    render_template
)
from TriangleProblem import app

@app.route('/', endpoint='index')
def index():
    return render_template("index.html")