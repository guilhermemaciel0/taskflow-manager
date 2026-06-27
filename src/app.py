from flask import Flask, request, redirect, render_template_string
from task_manager import create_task, list_tasks, update_task_status, delete_task

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>TaskFlow Manager</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
            padding: 30px;
        }

        .container {
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 0 10px #ccc;
        }

        h1 {
            color: #1f4e79;
        }

        form {
            margin-bottom: 20px;
        }

        input, textarea, select, button {
            padding: 10px;
            margin: 5px 0;
            width: 100%;
            box-sizing: border-box;
        }

        button {
            background: #1f4e79;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }

        button:hover {
            background: #163b5c;
        }

        .task {
            background: #eef3f8;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 10px;
        }

        .status {
            font-weight: bold;
            color: #0a6b35;
        }

        .delete {
            background: #b00020;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>TaskFlow Manager</h1>
        <p>Sistema web básico de gerenciamento de tarefas.</p>

        <h2>Criar nova tarefa</h2>

        <form action="/create" method="POST">
            <input type="text" name="title" placeholder="Título da tarefa" required>
            <textarea name="description" placeholder="Descrição da tarefa"></textarea>
            <button type="submit">Adicionar tarefa</button>
        </form>

        <h2>Lista de tarefas</h2>

        {% if tasks %}
            {% for task in tasks %}
                <div class="task">
                    <h3>{{ task.title }}</h3>
                    <p>{{ task.description }}</p>
                    <p>Status: <span class="status">{{ task.status }}</span></p>

                    <form action="/update/{{ task.id }}" method="POST">
                        <select name="status">
                            <option value="Pendente">Pendente</option>
                            <option value="Em Progresso">Em Progresso</option>
                            <option value="Concluído">Concluído</option>
                        </select>
                        <button type="submit">Atualizar status</button>
                    </form>

                    <form action="/delete/{{ task.id }}" method="POST">
                        <button class="delete" type="submit">Excluir tarefa</button>
                    </form>
                </div>
            {% endfor %}
        {% else %}
            <p>Nenhuma tarefa cadastrada.</p>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML, tasks=list_tasks())


@app.route("/create", methods=["POST"])
def create():
    title = request.form.get("title")
    description = request.form.get("description")

    create_task(title, description)

    return redirect("/")


@app.route("/update/<int:task_id>", methods=["POST"])
def update(task_id):
    status = request.form.get("status")

    update_task_status(task_id, status)

    return redirect("/")


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    delete_task(task_id)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)