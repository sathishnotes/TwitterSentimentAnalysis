import sys
import json
import string

def lines(fp):
    print str(len(fp.readlines()))

def createDictionary(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def findSentScore(sentDictionary,tweet):
    sentScore = 0
    nonDictItems = []
    for term in tweet.split(' '):
        if term in sentDictionary:
            sentScore = sentScore + sentDictionary[term]
        else:
            nonDictItems.append(term)
    return sentScore,nonDictItems

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentDictionary = createDictionary(sent_file)
    specialChars = set(string.punctuation)
    for line in tweet_file:
        decodeText = json.loads(line.encode('utf8'))
        if 'text' in decodeText.keys():
            tweet = ''.join(x for x in (decodeText['text'].encode('utf8')).lower() if x not in specialChars)
            sentScore,nonDictItems = findSentScore(sentDictionary,tweet)
            for word in nonDictItems:
                wordLength = float(len(tweet)-len(nonDictItems))
                if wordLength != 0:
                    print word,sentScore/wordLength
                else:
                    print word,sentScore

if __name__ == '__main__':
    main()
