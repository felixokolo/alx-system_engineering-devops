#!/usr/bin/python3
"""API testing module"""
import json
import sys
from urllib import request

"""API request for user todo list"""
if __name__ == '__main__':
    if (len(sys.argv) < 2):
        exit()
    api_url_base = 'https://jsonplaceholder.typicode.com/'
    req_url = api_url_base + 'users/' + sys.argv[1]
    name = json.loads(request.urlopen(req_url).read().
                      decode('utf-8')).get('name')
    req_url = api_url_base + 'todos?userId=' + sys.argv[1]
    response = request.urlopen(req_url)
    resp = response.read().decode('utf-8')
    resp_list = json.loads(resp)
    done_list = [x for x in resp_list if x.get('completed')]
    print('Employee {} is done with tasks({}/{}):'.format(name,
                                                          len(done_list),
                                                          len(resp_list)))
    for x in done_list:
        print('\t {}'.format(x.get('title')))
