#!/usr/bin/python3
import json

with open('hotposts', 'r') as f:
    d = json.loads(f.read())
    post = d['data']['children'][0]
    print(post['data']['title'])
