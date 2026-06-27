tasks = []


def create_task(title, description):
    if not title:
        raise ValueError("O título da tarefa é obrigatório.")

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "status": "Pendente"
    }

    tasks.append(task)
    return task


def list_tasks():
    return tasks