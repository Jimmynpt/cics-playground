from flask import Flask, jsonify, redirect, url_for, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.config import Config


db = SQLAlchemy()
ma = Marshmallow() # for serialization

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.json.ensure_ascii = False  # convert unicode to chinese

    db.init_app(app)
    ma.init_app(app)
    
    with app.app_context():
        # Import routes here to avoid circular imports
        from app.auth.controllers import mod as auth_module
        from app.programme.controllers import mod as prog_module
        from app.form.controllers import mod as form_module

        # register blueprint
        app.register_blueprint(auth_module)
        app.register_blueprint(prog_module)
        app.register_blueprint(form_module)

    return app