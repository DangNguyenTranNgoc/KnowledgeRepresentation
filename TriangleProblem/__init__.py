import os
from flask import (
    Flask,
    render_template
)

def create_app(config=None):
    '''
    Create and configure an instance of the Flask application.
    '''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'Knowledge@Representation'
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

app = create_app()

from .routes import index
from .routes import triangle
