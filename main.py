from rich import print
from rich.console import  Console
from rich.progress import Progress, track
import time

from rich.prompt import Prompt

from repositories.todos_repository import initialize_todos_csv
from repositories.users_repository import initialize_users_csv
from views.auth_view import auth_menu
from views.main_view import main_menu


def splash_screen():
    print (
    r"""
    (\ 
    \'\ 
     \'\     __________  
     / '|   ()_________)        [bold][green] TODO LIST APP [/green][/bold]
     \ '/    \ ~~~~~~~~ \       [info] by: James Paul Pandan [/info]
       \       \ ~~~~~~   \     [gray] version 1.0 [/gray]
       ==).      \__________\
      (__)       ()__________)  
            [gray] ASCII art: www.asciiart.eu [/gray]
    """
    )

def initialize():
    console = Console()
    console.clear()
    splash_screen()
    with Progress(console=console) as p:
        task1 = p.add_task("[green]Initializing....[/green]", total=100)

        initialize_users_csv()
        p.update(task1, advance=50)
        initialize_todos_csv()
        p.update(task1, advance=50)

    Prompt.ask("Press Enter to continue...")


if __name__ == '__main__':

    initialize()
    while True:
        user = auth_menu()
        main_menu(user)
