#!/usr/bin/python3
"""Export all employees' TODO tasks to a JSON file."""

import json

import requests


def main():
    """Organize all employees' tasks and export them to JSON."""
    users_response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    if users_response.status_code == 200:
        users = users_response.json()

        todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos"
        )

        if todos_response.status_code == 200:
            todos = todos_response.json()

            all_tasks = {}
            usernames = {}

            for user in users:
                user_id = user.get("id")
                username = user.get("username")

                all_tasks[str(user_id)] = []
                usernames[user_id] = username

            for task in todos:
                user_id = task.get("userId")

                task_data = {
                    "username": usernames.get(user_id),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                }

                all_tasks.get(str(user_id)).append(task_data)

            with open("todo_all_employees.json", "w") as json_file:
                json.dump(all_tasks, json_file)


if __name__ == "__main__":
    main()
