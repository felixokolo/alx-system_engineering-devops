#!/usr/bin/python3
"""API testing module"""
import csv
import json
import sys
from urllib import request

"""API request for user todo list"""
if __name__ == '__main__':
    if (len(sys.argv) < 2):
        exit()
    api_url_base = 'https://jsonplaceholder.typicode.com/'
    req_url = api_url_base + 'users/' + sys.argv[1]
    user_details = json.loads(request.urlopen(req_url).read().
                              decode('utf-8'))
    uname = user_details.get("username")
    uid = user_details.get('id')
    req_url = api_url_base + 'todos?userId=' + sys.argv[1]
    response = request.urlopen(req_url)
    resp = response.read().decode('utf-8')
    resp_list = json.loads(resp)
    done_list = [x for x in resp_list if x.get('completed')]
    emp_rec = [[str(uid), str(uname),
                str(x.get('completed')).lower(),
                x.get('title')] for x in resp_list]
    with open(str(uid) + '.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_ALL)
        for row in emp_rec:
            csv_writer.writerow(row)
