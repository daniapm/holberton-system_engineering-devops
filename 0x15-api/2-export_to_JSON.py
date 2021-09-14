#!/usr/bin/python3
"""
 Using what you did in the task #0, extend your Python
 script to export data in the JSON forma
"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    url_emp = 'https://jsonplaceholder.typicode.com/users/{}'\
              .format(sys.argv[1])
    url_task = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
               .format(sys.argv[1])
    response_task = requests.get(url_task).json()
    response_emp = requests.get(url_emp).json()
    username = response_emp['username']
    list = []
    for task in response_task:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        list.append(task_dict)
    js = {}
    js[sys.argv[1]] = list
    with open("{}.json".format(sys.argv[1]), 'w') as jsonfile:
        json.dump(js, jsonfile)
