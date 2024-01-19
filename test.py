from api_alchemy.twitter.tweet import Tweets

import json
 
# Opening JSON file
with open('sample.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)

tweet = Tweets(response=json_object)

for twt in tweet._tweets:
    print(twt._tweet)
    break