import uuid
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from models.todos import Todo
from models.users import User
from repositories import todos_repository

def display_todos(user: User):
    console = Console()
    console.clear()
    table = Table(title="Todos")
    table.add_column("No.")
    table.add_column("Title")
    table.add_column("Description")
    table.add_column("Status")
    table.add_column("Created At")
    table.add_column("Updated At")

    todos = todos_repository.get_todos_by_user_id(str(user.id))

    for index, todo in enumerate(todos):
        if todo.status == "PENDING":
            status = "[yellow]PENDING[/yellow]"
        elif todo.status == "DONE":
            status = "[green]DONE[/green]"
        else:
            status = "[red]CANCELLED[/red]"

        table.add_row(
            str(index + 1),
            todo.title,
            todo.description,
            status,
            str(todo.created_at),
            str(todo.updated_at),
        )
    console.print(table)
    return todos


def create_todo_view(user: User):

    console = Console()
    console.print("Create Todo")

    title = Prompt.ask('Title')
    description = Prompt.ask('Description')
    created_at = datetime.now()
    updated_at = datetime.now()

    todo = Todo(
        id = uuid.uuid4(),
        title=title,
        description=description,
        user_id=user.id,
        status="PENDING",
        created_at=created_at,
        updated_at=updated_at
    )

    todos_repository.create_todo(todo)
    console.print('Todo created successfully')
    console.input('Press Enter to continue...')
    return todo



def view_todos(user: User):

    console = Console()
    display_todos(user)
    console.input('Press Enter to continue...')



def update_todo_view(user: User):

    console = Console()
    todos = display_todos(user)

    console.print('[yellow]Press Ctrl+C to return to the main menu[/yellow]')
    index = Prompt.ask('Select an item to update', choices=[str(i + 1) for i in range(len(todos))])
    selected = todos[int(index) - 1]

    console.print('----------------------------------------------------------------------------')

    console.print(f'Title: [yellow] {selected.title} [/yellow]')
    selected.title = console.input('Update the Title to: ')
    console.print()

    console.print(f'Title: [yellow] {selected.description} [/yellow]')
    selected.description = console.input('Update the Description: ')
    console.print()

    console.print(f'Status: [yellow] {selected.status} [/yellow]')
    selected.status = Prompt.ask('Update the Status', choices=['PENDING', 'DONE', 'CANCELLED'])
    console.print()

    selected.updated_at = datetime.now()

    todos_repository.update_todo_by_id(selected.id, selected)

    console.print('[green]Todo updated successfully[/green]')
    console.input('Press Enter to continue...')




def delete_todo_view(user: User):

    console = Console()
    todos = display_todos(user)

    console.print('[yellow]Press Ctrl+C to return to the main menu[/yellow]')
    index = Prompt.ask('Select an item to delete', choices=[str(i + 1) for i in range(len(todos))])
    selected = todos[int(index) - 1]

    todos_repository.delete_todo_by_id(selected.id)

    console.print('[red]Todo deleted successfully[/red]')
    console.input('Press Enter to continue...')

