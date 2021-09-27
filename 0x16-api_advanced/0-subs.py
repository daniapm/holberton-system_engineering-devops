#!/usr/bin/python3
# function that queries the Reddit API and returns the number of
# subscribers (not active users, total subscribers) for a given
# subreddit. If an invalid subreddit is given, the function should return 0.
import requests


def number_of_subscribers(subreddit):

    url = "https://old.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'user_agent'}
    page = requests.get(url, headers=headers, allow_redirects=False)

    if page.status_code == 200:
        return page.json().get('data').get("subscribers")
    return 0
