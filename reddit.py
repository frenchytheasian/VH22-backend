import requests
from pprint import pprint

from reddit_auth import get_auth_headers

headers = get_auth_headers()

def get_id_from_url(url):
    return url.split('/')[6]

def get_top_n_posts(subreddit, n):
    url = f'https://oauth.reddit.com/r/{subreddit}/hot'
    posts = requests.get(url, headers=headers, params={'limit': n}).json()
    post_ids = [post['data']['id'] for post in posts['data']['children']]
    return post_ids

def get_all_comments_from_post(post_id):
    url = f'https://oauth.reddit.com/comments/{post_id}'
    comments = requests.get(url, headers=headers).json()
    comment_bodies = []
    for comment in comments[1]['data']['children']:
        try:
            comment_bodies.append(comment['data']['body'])
        except:
            pass
    return comment_bodies
        
if __name__ == "__main__":
    pprint(get_all_comments_from_post(get_top_n_posts('news', 1)[0]))
