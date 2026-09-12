"""
Gerenciador de Tarefas (Task Manager) - CLI simples.

Projeto de estudo para a disciplina de DevOps: pequena aplicacao
usada para praticar Git (branches, commits, pull requests) e
integracao continua (CI) com GitHub Actions.
"""
import json
import os
import sys
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks(path=DATA_FILE):
    """Carrega as tarefas do arquivo JSON. Retorna lista vazia se o arquivo nao existir."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks, path=DATA_FILE):
    """Salva a lista de tarefas no arquivo JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(tasks, description):
    """Adiciona uma nova tarefa a lista e a retorna."""
    new_id = max((t["id"] for t in tasks), default=0) + 1
    task = {
        "id": new_id,
        "description": description,
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    """Marca uma tarefa como concluida. Retorna True se encontrada."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


def remove_task(tasks, task_id):
    """Remove uma tarefa pelo id. Retorna True se removida."""
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            return True
    return False


def list_tasks(tasks):
    """Retorna uma lista de strings formatadas para exibicao."""
    lines = []
    for task in tasks:
        status = "x" if task["done"] else " "
        lines.append("[{}] #{} - {}".format(status, task["id"], task["description"]))
    return lines


def print_usage():
    print("Uso:")
    print('  python app.py add "descricao da tarefa"')
    print("  python app.py list")
    print("  python app.py done <id>")
    print("  python app.py remove <id>")


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print_usage()
        return 1

    command = argv[0]
    tasks = load_tasks()

    if command == "add" and len(argv) >= 2:
        task = add_task(tasks, " ".join(argv[1:]))
        save_tasks(tasks)
        print("Tarefa adicionada: #{} - {}".format(task["id"], task["description"]))
    elif command == "list":
        lines = list_tasks(tasks)
        print("\n".join(lines) if lines else "Nenhuma tarefa cadastrada.")
    elif command == "done" and len(argv) >= 2:
        ok = complete_task(tasks, int(argv[1]))
        save_tasks(tasks)
        print("Tarefa concluida!" if ok else "Tarefa nao encontrada.")
    elif command == "remove" and len(argv) >= 2:
        ok = remove_task(tasks, int(argv[1]))
        save_tasks(tasks)
        print("Tarefa removida!" if ok else "Tarefa nao encontrada.")
    else:
        print_usage()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
