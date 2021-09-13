#!/usr/bin/python3
"""
 Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress
"""
import csv
import requests
import sys

if __name__ == '__main__':
    url_emp = 'https://jsonplaceholder.typicode.com/users/{}'\
              .format(sys.argv[1])
    url_task = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
               .format(sys.argv[1])
    response_task = requests.get(url_task).json()
    response_emp = requests.get(url_emp).json()
    name = response_emp['username']
    with open('{}.csv'.format(sys.argv[1]), 'w') as f:
        writer = csv.writer(f)
        list = {}
        for task in response_task:
            list = (sys.argv[1], name, task['completed'], task['title'])
            writer.writerow(list)
