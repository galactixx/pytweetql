# pytweetql
![Tests](https://github.com/galactixx/pytweetql/actions/workflows/continuous_integration.yaml/badge.svg)
![PyPI Downloads](https://static.pepy.tech/badge/pytweetql/month)
![PyPI Downloads](https://static.pepy.tech/badge/pytweetql)

pytweetql is a simple Python package designed for developers who work with the Twitter GraphQL API

Currently it is built to parse tweet, user, and list GET responses from the Twitter GraphQL API. The function to call is based on the GraphQL endpoint. So for the UserTweets endpoint, you would import the ```parsing``` module and use the ```parse_user_tweets()``` function.

## How it Works

```python
from pytweetql import parsing

# Given a response from GraphQL
response = {'data': {.....}}

# To pull data from a tweet response
tweets = parsing.parse_user_tweets(response=response)

# Will return a list of tweet classes, one for each tweet parsed
print(tweets.tweets)


# To pull data from a user response
users = parsing.parse_users_by_screen_name(response=response)

# Will return a list of user classes, one for each user parsed
print(users.users)


# To pull data from a list response
lists = parsing.parse_create_list(response=response)

# Will return a list of list classes, one for each list parsed
print(lists.lists)

```
