#!/usr/bin/python3
"""Export an employee's TODO list data to JSON."""

import json
import requests
import sys


def main():
    """Export all employee TODO tasks to a JSON file."""
    employee_id = int(sys.argv[1])

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            employee_id
        )
    )

    if response.status_code == 200:
        user_data = response.json()
        todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos",
            params={"userId": employee_id}
        )

        if todos_response.status_code == 200:
            todos = todos_response.json()
            username = user_data.get("username")

            tasks = [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username
                }
                for task in todos
            ]

            filename = "{}.json".format(employee_id)

            with open(filename, "w") as json_file:
                json.dump(
                    {str(employee_id): tasks},
                    json_file
                )


if __name__ == "__main__":
    main()

