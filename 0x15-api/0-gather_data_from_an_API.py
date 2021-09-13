#!/usr/bin/python3
import requests
import sys
import json

if __name__ == '__main__':
    url_emp = 'https://jsonplaceholder.typicode.com/users/{}'
    .format(sys.argv[1])
    url_task = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    .format(sys.argv[1])
    response_emp = requests.get(url_emp)
    employee = response_emp.json()
    response_task = requests.get(url_task)
    tasks = response_task.json()
    count = 0
    tittle = []
    for task in tasks:
        if task['completed']:
            count += 1
            tittle.append(task['title'])
    print('Employee {} is done with tasks({}/{})'
          .format(employee['name'], count, len(tasks)))
    for element in tittle:
        print("\t ", element)
