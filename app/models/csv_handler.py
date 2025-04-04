import csv
from app.models import db
from app.models import Task
file_path="/home/linux/Projects/flask-task-manager/task.csv"

class CSVHandler:
    @staticmethod
    def import_tasks(file_path):
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                new_task = Task(title=row["title"], description=row["description"])
                db.session.add(new_task)
            db.session.commit()
