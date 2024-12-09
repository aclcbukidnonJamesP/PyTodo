
# Introduction

This project is a simple ToDo List application built using
Python. It allows users to manage their task by adding,
viewing, updating and deleting tasks.

The tasks are stored in a **CSV File** which is created
ensures that the tasks are persisted even after the program
is closed.

This project also uses the [Rich](https://github.com/Textualize/rich) library to display a visually
appealing command interface to the user.



## Features
- Add a task
  - Adds new task with a title and description

- View Tasks
  - Displays all tasks in a table format

- Update Task
  - Updates the title and description of a task

- Delete Task
  - Deletes a task from the list
  
- Persistent Storage
  - Tasks are stored in a CSV file

- Basic User Management
  - Users can create an account and login to manage their tasks


## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/aclcbukidnonJamesP/PyTodo.git
   cd PyTodo
    ```
2. Install the dependencies
    ```bash
    pip install rich
    ```
3. Run the application
   ```bash
   python main.py
   ```

## Usage
```bash
python main.py
```

## Project Structure
```
├───data 
├───models
├───repositories
└───views
```
- Data
  - Contains the CSV file where the tasks are stored
- Models
  - Contains the Task and User models
  - Task: Represents a task with a title and description
  - User: Represents a user with a username and password
- Repositories
  + Contains the TaskRepository and UserRepository
  + TaskRepository: Handles the CRUD operations for tasks
  + UserRepository: Handles the CRUD operations for users
- Views
    - Contains the user interface for the application
    - The views are built using the [Rich](https://github.com/Textualize/rich) library
    - The views include the main menu, login, register, task list, add task, update task, and delete task views