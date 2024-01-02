#!/usr/bin/python3
"""
request user todo tasks from
https://jsonplaceholder.typicode.com using
employee id provided and export it to a csv file
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

    with open(f'{emp_id}.csv', 'w') as csv_file:
        for task in resp_todo.json():
            csv_file.write(
                    f""""{emp_id}","{name}","{task['completed']}",
                        "{task['title']}\n""")
