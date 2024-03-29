from flask import Flask, render_template
#database imports
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import config

db = SQLAlchemy()
moment = Moment()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # attach error pages and routes here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app