#!/usr/bin/python3
"""
a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """the module"""
    if counts is None:
        counts = {}

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    articles = data["data"]["children"]
    titles = [article["data"]["title"].lower() for article in articles]

    for title in titles:
        for word in word_list:
            if word.lower() in title:
                counts[word.lower()] = counts.get(word.lower(), 0) + 1

    after = data["data"]["after"]
    if after is not None:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
