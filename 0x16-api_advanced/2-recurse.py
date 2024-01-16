#!/usr/bin/python3
"""return list of all hot posts in a subreddit"""
import requests


def set_up():
    """return list of all hot posts in a subreddit"""
    CLIENT_ID = "FFDu9MetkGi_k_ddGyZPDw"
    SECRET_KEY = "0PXLIPopm_b3K_hAugxar6emQLqU7A"
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

    data = {
            'grant_type': 'password',
            'username': 'gisconesheri',
            'password': 'L5M3n8RYcCiLcx'
            }

    headers = {'User-Agent': 'ALXAPI/1.0'}
    response = requests.post("https://www.reddit.com/api/v1/access_token",
                             auth=auth, data=data, headers=headers)
    TOKEN = response.json()['access_token']

    headers['Authorization'] = 'bearer {}'.format(TOKEN)
    return headers


def recurse(subreddit, hot_list = [], params = {'limit': 100}, count = 0):

    headers = set_up()

    resp = requests.get(f'https://oauth.reddit.com/r/{subreddit}/hot',
                        headers=headers, params=params, allow_redirects=False)
    if resp.status_code == 200:
        d = resp.json()
        for post in d['data']['children']:
            count += 1
            hot_list.append(post['data']['title'])
        params['after'] = d['data']['after']
        params['count'] = count
        if params['after'] is None:
            return hot_list

        recurse(subreddit)
        return hot_list
    return None
