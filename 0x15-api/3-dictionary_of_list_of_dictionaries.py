#!/usr/bin/python3
"""API testing module"""
import csv
import json
import sys
from urllib import request

"""API request for user todo list"""
if __name__ == '__main__':
    api_url_base = 'https://jsonplaceholder.typicode.com/'
    req_url = api_url_base + 'users/'
    user_details = json.loads(request.urlopen(req_url).read().
                              decode('utf-8'))
    req_url = api_url_base + 'todos'
    response = request.urlopen(req_url)
    resp = response.read().decode('utf-8')
    resp_list = json.loads(resp)
    emp_rec = {}
    for user_detail in user_details:
        uname = user_detail.get("username")
        uid = user_detail.get('id')
        emp_rec[str(uid)] = [{'task': x.get('title'),
                              'completed': x.get('completed'),
                              'username': uname}
                             for x in resp_list if x.get('userId') == uid]
    with open('todo_all_employees.json', 'w') as jsonwriter:
        json.dump(emp_rec, jsonwriter)
