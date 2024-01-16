#!/usr/bin/python3
import requests
import sys


def number_of_subscribers(subreddit):
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

    resp = requests.get(f'https://oauth.reddit.com/r/{subreddit}/about',
                        headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        return resp.json()['data']['subscribers']
    else:
        return 0
