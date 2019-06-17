import sys
import json
import string
from collections import defaultdict

def createDictionary(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def findSentScore(sentDictionary,tweet):
    sentScore = 0
    for term in tweet.split(' '):
        if term in sentDictionary:
            sentScore = sentScore + sentDictionary[term]
    return sentScore

def geoInfo(tweet):
    try:
        if tweet['place']['country_code'] == 'US':
            state = tweet['place']['full_name'][-2:]
            return True,state
        else:
            return False,''
    except:
        pass
    return False,''

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentDictionary = createDictionary(sent_file)
    specialChars = set(string.punctuation)
    state_happy_index = defaultdict()
    total_tweet_count = 0
    for line in tweet_file:
        decodeText = json.loads(line.encode('utf8'))
        try:
            if decodeText['lang'] == 'en':
                if 'text' in decodeText.keys():
                    tweet = ''.join(x for x in (decodeText['text'].encode('utf8')).lower() if x not in specialChars)
                    is_US,state = geoInfo(decodeText)
                    if is_US:
                        total_tweet_count += 1
                        sentScore = findSentScore(sentDictionary,tweet)
                        if state in state_happy_index:
                            state_happy_index[state] += sentScore
                        else:
                            state_happy_index[state] = sentScore
        except:
            pass

    happiest_state = 'YY'
    happy_score = -1
    for state,score in state_happy_index.items():
        if score > happy_score:
            happy_score = score
            happiest_state = state
    print happiest_state

if __name__ == '__main__':
    main()
