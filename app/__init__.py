# This file marks the app directory as a Python package
from .app import app
from .config import Config
from .data_fetcher import fetch_data
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Import configuration
    
     # Import routes here or register blueprints
    from .app import app as main_app
    app.register_blueprint(main_app)
    
    return app
