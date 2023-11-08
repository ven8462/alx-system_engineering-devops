#!/usr/bin/python3
"""
 Reddit APIs
"""
from requests import get


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 2'
    }
    response = get(url, headers=headers, allow_redirects=False)
    reddits = response.json()

    try:
        children = reddits.get('data').get('children')
        for i in range(10):
            print(children[i].get('data').get('title'))
    except Exception:
        print('None')
