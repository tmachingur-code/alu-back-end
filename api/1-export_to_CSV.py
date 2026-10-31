#!/usr/bin/python3
"""Export an employee's TODO list data to CSV."""

import csv
import sys

import requests


def main():
    """Export all employee TODO tasks to a CSV file."""
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

            filename = "{}.csv".format(employee_id)

            with open(filename, "w", newline="") as csv_file:
                writer = csv.writer(
                    csv_file,
                    quoting=csv.QUOTE_ALL
                )

                for task in todos:
                    writer.writerow([
                        employee_id,
                        username,
                        task.get("completed"),
                        task.get("title")
                    ])


if __name__ == "__main__":
    main()
