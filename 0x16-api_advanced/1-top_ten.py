#!/usr/bin/python3
"""
function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given, the
function should return 0.
"""
import requests


def top_ten(subreddit):
    """
    Funtion top_ten that return top hot post
    """

    url = "https://old.reddit.com/r/{}/hot.json?limit=10".format(
        subreddit)
    headers = {'User-Agent': 'user_agent'}
    page = requests.get(url, headers=headers, allow_redirects=False)

    if page.status_code == 200:
        tittle = page.json()['data']['children']
        for post in tittle:
            print(post['data']['title'])
    else:
        return print("None")
