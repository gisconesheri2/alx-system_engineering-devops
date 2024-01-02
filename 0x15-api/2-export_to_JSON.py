#!/usr/bin/python3
"""
request user todo tasks from
https://jsonplaceholder.typicode.com using provided id
and export all tasks in json format
"""
import json
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]

    resp_todo = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos')

    resp_user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{emp_id}')
    name = resp_user.json().get('name')

    task_dict = {}
    task_list = []

    for task in resp_todo.json():
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = name
        task_list.append(task_dict)
        task_dict = {}

    py_struct = {}
    py_struct[emp_id] = task_list

    with open(f'{emp_id}.json', 'w') as json_file:
        json.dump(py_struct, json_file)
