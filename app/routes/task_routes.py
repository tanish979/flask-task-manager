from flask import Blueprint, request, jsonify
from app.models import db  
from app.models.task import TaskManager  


task_bp = Blueprint("task", __name__)

@task_bp.route("/", methods=["GET"])
def home():
    return "Hello, Flask is running!"

@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = TaskManager.query.all()
    return jsonify({"tasks": [task.to_dict() for task in tasks]})

@task_bp.route("/task", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "title" not in data or "description" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    new_task = TaskManager(title=data["title"], description=data["description"])
    db.session.add(new_task)
    db.session.commit()

    return jsonify({"message": "Task created successfully"}), 201
