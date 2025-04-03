from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Define db here

from app.models.task import TaskManager  # Import TaskManager
