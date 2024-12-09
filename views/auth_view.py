import uuid

from rich.console import Console
from rich.prompt import Prompt

from models.users import User
from repositories import users_repository


def login() -> User | None:

    console = Console()
    try:
        while True:
            console.clear()
            console.print('Enter your credentials')
            console.print('[yellow]Press Ctrl+C to return to the main menu[/yellow]')
            console.print('------------------------------------------------------------')
            username = Prompt.ask('Email')
            password = Prompt.ask('Password', password=True)

            user = users_repository.get_user_by_email(username)
            if user is not None and user.password == password:
                console.print('Successfully logged in!\n\n', style='green')
                console.print(f'Welcome [green]{user.first_name} {user.last_name}[/green]')

                Prompt.ask('Press Enter to continue...')
                return user


            console.print('[red]Invalid credentials[/red]')

            Prompt.ask('Press Enter to continue...')

    except KeyboardInterrupt:
        return None




def register() -> User | None:
    console = Console()
    console.print("Register")
    console.print('[yellow]Press Ctrl+C to return to the main menu[/yellow]')
    try:
        last_name = Prompt.ask('Last Name')
        first_name = Prompt.ask('First Name')
        email = Prompt.ask('Email')
        password = Prompt.ask('Password', password=True)

        user = User(
            id = uuid.uuid4(),
            last_name=last_name,
            first_name=first_name,
            email=email,
            password=password
        )

        users_repository.create_user(user)
        console.print('User created successfully')
        return user
    except KeyboardInterrupt:
        return None


def auth_menu() -> User:
    while True:
        console = Console()
        console.clear()
        console.print('[bold]Authentication[/bold]')

        console.print('1. Login')
        console.print('2. Register')
        console.print('3. Exit')

        choice = Prompt.ask('Choose an option', choices=['1', '2', '3'])
        console.clear()
        if choice == '1':
            user = login()
            if user is None:
                continue
            return user
        elif choice == '2':
            user = register()
            if user is None:
                continue
            return user
        else:
            exit()

