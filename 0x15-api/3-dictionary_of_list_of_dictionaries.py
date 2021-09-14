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
    for user in response_emp:
        user = user.get('username')
    for task in response_task:
        task_dict = {}
        task_dict["username"] = user
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        id = task.get('userId')
        list.append(task_dict)
    js = {}
    js[task.get('id')] = list
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(js, jsonfile)
