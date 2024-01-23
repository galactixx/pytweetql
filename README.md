# pytweetql
pytweetql is a simple Python package designed for developers who work with the Twitter GraphQL API

Currently it is built to parse tweet, user, and list GET responses from the Twitter GraphQL API. Will most likely expand to include POST responses, all Twitter APIs (v1.1 and v2) and then possibly add other APIs (Spotify, Instagram, etc..).

## How it Works

```python
from pytweetql import parsing

# Given a response from GraphQL
response = {'data': {.....}}

# To pull data from a tweet response
tweets = parsing.parse_tweets(response=response)

# Will return a list of tweet classes, one for each tweet parsed
print(tweets.tweets)


# To pull data from a user response
users = parsing.parse_users(response=response)

# Will return a list of user classes, one for each user parsed
print(users.users)


# To pull data from a list response
lists = parsing.parse_lists(response=response)

# Will return a list of list classes, one for each list parsed
print(lists.lists)

```
