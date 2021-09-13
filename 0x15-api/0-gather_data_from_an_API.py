#!/usr/bin/python3
"""
 Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == '__main__':
    url_emp = 'https://jsonplaceholder.typicode.com/users/{}'\
              .format(sys.argv[1])
    url_task = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
               .format(sys.argv[1])
    response_emp = requests.get(url_emp)
    employee = response_emp.json()
    response_task = requests.get(url_task)
    tasks = response_task.json()
    list_task = []
    for task in tasks:
        if task.get('completed') is True:
            list_task.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".
          format(employee.get('name'), len(list_task), len(tasks)))
    print("\n".join("\t {}".format(task) for task in list_task))
