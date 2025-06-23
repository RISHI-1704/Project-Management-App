# Project Management App

## Usage

The Project Management App is a web-based application that allows users to create, manage, and collaborate on projects and tasks. The main features of the app include:

- Creating and managing projects
- Creating and assigning tasks to users
- Viewing project details and associated tasks
- Deleting projects and tasks
- Creating and managing user accounts

To use the app, follow these steps:

1. Navigate to the project's main page.
2. Click on the "Create New Project" button to create a new project.
3. Fill out the project details and click "Submit" to create the project.
4. Click on the project name to view the project details page.
5. On the project details page, you can add tasks, assign users to tasks, and delete tasks.
6. To create a new user, click on the "Create New User" button.
7. To delete a user, click on the "All Users" button and then click the "Delete User" button next to the user you want to delete.

## API

The Project Management App provides the following API endpoints:

| Endpoint | HTTP Method | Description |
| --- | --- | --- |
| `/` | GET | List all projects |
| `/create-project/` | POST | Create a new project |
| `/create-tasks/` | POST | Create a new task |
| `/delete-project/<int:pk>` | DELETE | Delete a project |
| `/delete-task/<int:pk>` | DELETE | Delete a task |
| `/create-user` | POST | Create a new user |
| `/delete-user/<int:pk>` | DELETE | Delete a user |
| `/remove-user/<int:task_id>/<int:user_id>` | POST | Remove a user from a task |
| `/project_details/<int:pk>` | GET | View details of a project |
| `/edit-task/<int:pk>` | PUT | Edit a task |
| `/all-users` | GET | List all users |

