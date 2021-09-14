#!/usr/bin/python3
"""
 Using what you did in the task #0, extend your Python
 script to export data in the JSON forma
"""
import json
import requests

if __name__ == '__main__':
    url_emp = 'https://jsonplaceholder.typicode.com/users'
    url_task = 'https://jsonplaceholder.typicode.com/todos'
    response_task = requests.get(url_task).json()
    response_emp = requests.get(url_emp).json()

    list = []
    task_dict = {}
    js = {}
    for users in response_emp:
        for task in response_task:
            if task.get('userId') == users.get('id'):
                task_dict["username"] = users.get('username')
                task_dict["task"] = task.get('title')
                task_dict["completed"] = task.get('completed')
                id = task.get('userId')
                list.append(task_dict)
        js[users.get('id')] = list
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(js, jsonfile)
