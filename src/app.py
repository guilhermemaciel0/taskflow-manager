from flask import Flask, request, jsonify
from task_manager import create_task, list_tasks, update_task_status, delete_task

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "TaskFlow Manager - Sistema de Gerenciamento de Tarefas"
    })


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    try:
        task = create_task(
            data.get("title"),
            data.get("description", "")
        )
        return jsonify(task), 201
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(list_tasks())


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    try:
        task = update_task_status(task_id, data.get("status"))
        return jsonify(task)
    except ValueError as error:
        return jsonify({"error": str(error)}), 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    try:
        delete_task(task_id)
        return jsonify({"message": "Tarefa removida com sucesso."})
    except ValueError as error:
        return jsonify({"error": str(error)}), 404


if __name__ == "__main__":
    app.run(debug=True)