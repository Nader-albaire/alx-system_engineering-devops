#!/usr/bin/python3
'''
gather employee data from API
'''

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

def get_employee_info(employee_id):
    try:
        response = requests.get(f'{REST_API}/users/{employee_id}')
        response.raise_for_status()  # Raise an exception for invalid response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching employee data: {e}")
        sys.exit(1)

def get_todo_list(employee_id):
    try:
        response = requests.get(f'{REST_API}/todos')
        response.raise_for_status()  # Raise an exception for invalid response
        return [task for task in response.json() if task['userId'] == employee_id]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching TODO list: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_info = get_employee_info(employee_id)
    todo_list = get_todo_list(employee_id)

    completed_tasks = [task['title'] for task in todo_list if task['completed']]

    print(f"Employee {employee_info['name']} is done with tasks({len(completed_tasks)}/{len(todo_list)}):")
    for task in completed_tasks:
        print(f"\t{task}")

