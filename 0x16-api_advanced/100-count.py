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


def count_words(subreddit, word_list, words_count = {}, params = {'limit': 100}, count = 0):

    headers = set_up()

    resp = requests.get(f'https://oauth.reddit.com/r/{subreddit}/hot',
                        headers=headers, params=params, allow_redirects=False)
    if resp.status_code == 200:
        d = resp.json()
        for post in d['data']['children']:
            count += 1
            title = post['data']['title'].lower().split()
            for word in word_list:
                word_occ = title.count(word)
                words_count[word] = words_count.get(word, 0) + word_occ
        params['after'] = d['data']['after']
        params['count'] = count
        if params['after'] is None:
            sort_wc = sorted(words_count.items(), key=lambda x:x[1], reverse=True)
            for word_tuple in sort_wc:
                if word_tuple[1] > 0:
                    print('{}: {}'.format(word_tuple[0], word_tuple[1]))
            return

        count_words(subreddit, word_list, words_count, params, count)
