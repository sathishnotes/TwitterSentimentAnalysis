import sys
import json
import string

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

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentDictionary = createDictionary(sent_file)
    specialChars = set(string.punctuation)
    for line in tweet_file:
        decodeText = json.loads(line.encode('utf8'))
        if 'text' in decodeText.keys():
            tweet = ''.join(x for x in (decodeText['text'].encode('utf8')).lower() if x not in specialChars)
            print findSentScore(sentDictionary,tweet)

if __name__ == '__main__':
    main()
