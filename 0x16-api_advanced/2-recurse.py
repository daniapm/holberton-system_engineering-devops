#!/usr/bin/python3
""" recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the
given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):

    url = "https://old.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'user_agent'}
    arg = {"after": after}
    page = requests.get(url, headers=headers, params=arg,
                        allow_redirects=False)
    tittle = page.json()['data']['children']
    after = page.json()['data']['after']

    if tittle is not None:
        for item in tittle:
            hot_list.append(item.get("data").get("title"))
    if after is not None:
        recurse(subreddit, hot_list, after)
    else:
        return print("None")
