API Project

## Project Description

This project focuses on using Python to interact with the JSONPlaceholder REST API. It retrieves employee information and TODO tasks, processes the data, and exports the results into CSV and JSON formats.

The project contains four tasks, covering API data retrieval, task progress tracking, and data export for individual employees and all employees.

## Usage

Clone the repository and navigate to the API directory:

```bash
git clone https://github.com/tmachingur-code/alu-back-end
cd alu-back-end/api
```

Run the scripts using Python 3:

```bash
# Task 0: Display an employee's completed tasks
python3 0-gather_data_from_an_API.py 1

# Task 1: Export an employee's tasks to CSV
python3 1-export_to_CSV.py 1

# Task 2: Export an employee's tasks to JSON
python3 2-export_to_JSON.py 1

# Task 3: Export all employees' tasks to JSON
python3 3-dictionary_of_list_of_dictionaries.py
```

Replace `1` with the employee ID you want to retrieve. Task 3 processes all employees and does not require an ID.

## What I Learned

- How REST APIs work and how to retrieve data using HTTP GET requests.
- How to use the Python `requests` library.
- How to process JSON data using Python dictionaries and lists.
- How to export data into CSV and JSON files.
- How to use list comprehensions, loops and dictionary operations.
- How to work with command-line arguments.
- How to check Python code style using `pycodestyle`.
- How to use Git for version control and project submission.
