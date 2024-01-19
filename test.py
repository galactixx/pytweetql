from api_alchemy.twitter.parsing.tweet import Tweets

import json
 
# Opening JSON file
with open('sample.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)

tweets = Tweets(response=json_object)
print(tweets.num_tweets)

for twt in tweets._tweets:
    print(twt._tweet)
    break