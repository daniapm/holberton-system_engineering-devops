#!/usr/bin/python3
"""
recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the
given subreddit, the function should return None.
"""
import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    headers = {'User-Agent': 'user_agent'}
    url = "https://www.reddit.com/r/{}/hot/.json?after={}".format(
        subreddit, after)
    page = requests.get(url, headers=headers)
    if page.status_code == 200:
        tittle = page.json()
        request = tittle.get('data').get('children')
        pagination = tittle.get('data').get('after')
        for titt in request:
            hot_list.append(titt.get("data").get("title"))
        if pagination is not None:
            return recurse(subreddit, hot_list,  pagination)
        else:
            return hot_list

    else:
        return None
