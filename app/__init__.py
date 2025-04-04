import os
from flask import Flask
from app.models import db 
from app.routes.task_routes import task_bp

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/database")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)  

    app.register_blueprint(task_bp, url_prefix="/")

    return app
