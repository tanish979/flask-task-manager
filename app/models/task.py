from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Ensure this is defined

class TaskManager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description}
