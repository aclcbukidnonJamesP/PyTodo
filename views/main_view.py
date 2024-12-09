from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from models.users import User
from views.todo_view import create_todo_view, view_todos, update_todo_view, delete_todo_view


def main_menu(user: User):
    console = Console()

    while True:
        console.clear()

        console.print(f"User: {user.last_name}, {user.first_name} ", style="bold green")
        console.print(f"Email: {user.email} ", style="bold green")
        table = Table(title="Main Menu")
        table.add_column("Option")
        table.add_column("Description")

        table.add_row("1", "View Tasks")
        table.add_row("2", "Create Task")
        table.add_row("3", "Update Task")
        table.add_row("4", "Delete Task", end_section=True)
        table.add_section()
        table.add_row("0", "Logout")


        console.print(table)

        choice = Prompt.ask('Select Option', choices = ['1', '2', '3', '4', '0'])


        try:
            if choice == '1':
                view_todos(user)
            elif choice == '2':
                create_todo_view(user)
                pass
            elif choice == '3':
                update_todo_view(user)
            elif choice == '4':
                delete_todo_view(user)
            elif choice == '0':
                return
            else:
                console.print('Invalid choice')
                Prompt.ask('Press Enter to continue...')
        except KeyboardInterrupt:
            continue






