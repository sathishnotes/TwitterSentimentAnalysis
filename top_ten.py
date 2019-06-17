import sys
import json
import string
from collections import defaultdict
import operator

def main():
    punc = (",./;'?&-#!@")
    specialChars = set(string.punctuation)
    tweet_file = open(sys.argv[1])
    hashtagDict = defaultdict()
    for line in tweet_file:
        decodeText = json.loads(line.encode('ascii','replace'))
        try:
            hashtags = decodeText['entities']['hashtags']
            hashTags = []
            for tags in hashtags:
                tweet = ''.join(x for x in (decodeText['text'].encode('ascii','replace')).lower().translate(None,punc) if x not in specialChars)
                hashTags.append(tweet)
            for hashtag in hashTags:
                if hashtag.strip() in hashtagDict:
                    hashtagDict[hashtag.strip()] += 1
                else:
                    hashtagDict[hashtag.strip()] = 1
        except:
            pass
    hashtagDict = sorted(hashtagDict.items(), key=operator.itemgetter(1),reverse=True)
    for i in range(10):
        print hashtagDict[i][0],float(hashtagDict[i][1])

if __name__ == '__main__':
    main()
