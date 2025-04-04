import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://marbal:123@db/task_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False