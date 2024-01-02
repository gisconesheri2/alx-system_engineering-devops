#!/usr/bin/python3
"""
request user todo tasks from
https://jsonplaceholder.typicode.com
and print out list of tasks completed for the user id provided
"""
import json
import requests
import sys

if __name__ == "__main__":

    resp_todo = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos')

    resp_user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}')
    name = resp_user.json()['name']

    completed = 0
    total_tasks = 0
    completed_titles = []

    for task in resp_todo.json():
        if task['completed'] is True:
            completed += 1
            completed_titles.append(task['title'])
        total_tasks += 1

print(f'Employee {name} is done with tasks({completed}/{total_tasks}):')
for title in completed_titles:
    print(f'\t {title}')
