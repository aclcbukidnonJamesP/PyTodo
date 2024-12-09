import os
import csv

from models.todos import Todo

todos_csv_file = 'data/todos.csv'
todo_csv_header = ["id", "title", "description", "user_id", "status", "created_at", "updated_at"]



def initialize_todos_csv():
    if os.path.exists(todos_csv_file):
        return

    with open(todos_csv_file, 'w', newline="") as file:
        csv_writer = csv.DictWriter(file, todo_csv_header)
        csv_writer.writeheader()



def create_todo(todo : Todo):

    with open(todos_csv_file, 'a', newline="") as file:
        csv_writer = csv.DictWriter(file, todo_csv_header)
        csv_writer.writerow(todo.__dict__)


def get_all_todos() -> list[Todo]:
    with open(todos_csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        todos = []
        for row in csv_reader:
            todo = Todo(
                id=row["id"],
                title=row["title"],
                description=row["description"],
                user_id=row["user_id"],
                status=row["status"],
                created_at=row["created_at"],
                updated_at=row["updated_at"]
            )
            todos.append(todo)
        return todos

def get_todo_by_id(todo_id) -> Todo | None:
    with open(todos_csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["id"] == todo_id:
                todo = Todo(
                    id=row["id"],
                    title=row["title"],
                    description=row["description"],
                    user_id=row["user_id"],
                    status=row["status"],
                    created_at=row["created_at"],
                    updated_at=row["updated_at"]
                )
                return todo
        return None


def get_todos_by_user_id(user_id) -> list[Todo]:
    with open(todos_csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        todos = []
        for row in csv_reader:
            if row["user_id"] == str(user_id):
                todo = Todo(
                    id=row["id"],
                    title=row["title"],
                    description=row["description"],
                    user_id=row["user_id"],
                    status=row["status"],
                    created_at=row["created_at"],
                    updated_at=row["updated_at"]
                )
                todos.append(todo)
        return todos


def update_todo_by_id(todo_id ,todo : Todo):
    todos = get_all_todos()
    for i in range(len(todos)):
        if todos[i].id == todo_id:
            todos[i] = todo
            break

    with open(todos_csv_file, 'w', newline="") as file:
        csv_writer = csv.DictWriter(file, todo_csv_header)
        csv_writer.writeheader()
        for todo in todos:
            csv_writer.writerow(todo.__dict__)


def delete_todo_by_id(todo_id):
    todos = get_all_todos()
    for i in range(len(todos)):
        if todos[i].id == todo_id:
            del todos[i]
            break

    with open(todos_csv_file, 'w', newline="") as file:
        csv_writer = csv.DictWriter(file, todo_csv_header)
        csv_writer.writeheader()
        for todo in todos:
            csv_writer.writerow(todo.__dict__)
