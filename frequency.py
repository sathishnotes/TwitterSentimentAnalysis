import sys
import json
import string

def main():
    punc = (",./;'?&-#!@")
    freqDictionary = {}
    tweet_file = open(sys.argv[1])
    specialChars = set(string.punctuation)
    for line in tweet_file:
        decodeText = json.loads(line.encode('ascii','replace'))
        if 'text' in decodeText.keys():
            tweet = ''.join(x for x in (decodeText['text'].encode('ascii','replace')).lower().translate(None,punc) if x not in specialChars)
            for word in tweet.split(' '):
                if word.strip() in freqDictionary:
                    freqDictionary[word.strip()] += 1
                else:
                    freqDictionary[word.strip()] = 1
    totalOccurences = sum(freqDictionary.values())
    for word in freqDictionary.keys():
        print word + " " + str(float(freqDictionary[word])/totalOccurences)

if __name__ == '__main__':
    main()
