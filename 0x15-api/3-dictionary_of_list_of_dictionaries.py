#!/usr/bin/python3
"""
request all user todo tasks from
https://jsonplaceholder.typicode.com and generate a json file
"""
import json
import requests


if __name__ == "__main__":

    resp_user = requests.get('https://jsonplaceholder.typicode.com/users')
    resp_user_json = resp_user.json()
    emp_id = 1
    py_struct = {}
    for user in resp_user_json:
        name = user['name']
        task_dict = {}
        task_list = []

        resp_todo = requests.get(
                f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos')

        for task in resp_todo.json():
            task_dict['username'] = name
            task_dict['task'] = task.get('title')
            task_dict['completed'] = task.get('completed')
            task_list.append(task_dict)
            task_dict = {}

        py_struct[emp_id] = task_list
        task_list = []
        emp_id += 1

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(py_struct, json_file)
