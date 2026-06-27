import sys
import os

sys.path.append(os.path.abspath("src"))

from task_manager import create_task, list_tasks, update_task_status, delete_task, tasks


def setup_function():
    tasks.clear()


def test_create_task():
    task = create_task("Estudar Engenharia de Software", "Criar projeto no GitHub")

    assert task["title"] == "Estudar Engenharia de Software"
    assert task["status"] == "Pendente"


def test_create_task_without_title():
    try:
        create_task("", "Descrição")
    except ValueError as error:
        assert str(error) == "O título da tarefa é obrigatório."


def test_list_tasks():
    create_task("Tarefa 1", "Descrição 1")
    create_task("Tarefa 2", "Descrição 2")

    assert len(list_tasks()) == 2


def test_update_task_status():
    task = create_task("Finalizar README", "Documentar projeto")
    updated_task = update_task_status(task["id"], "Concluído")

    assert updated_task["status"] == "Concluído"


def test_delete_task():
    task = create_task("Remover tarefa", "Teste de exclusão")
    result = delete_task(task["id"])

    assert result is True
    assert len(list_tasks()) == 0