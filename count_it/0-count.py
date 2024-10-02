#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after='', word_count={}):
    headers = {'User-Agent': 'python:word.count:v1.0 (by /u/your_username)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return
        data = response.json()
        articles = data.get('data', {}).get('children', [])
        for article in articles:
            title = article['data']['title'].lower().split()
            for word in word_list:
                lower_word = word.lower()
                word_count[lower_word] = word_count.get(lower_word, 0) + title.count(lower_word)
        after = data.get('data', {}).get('after', None)
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_word_count = sorted(
                [(word, count) for word, count in word_count.items() if count > 0],
                key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
    except:
        return
