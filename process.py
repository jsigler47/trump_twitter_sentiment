import sentiment_mod as s
import numpy as np
import pandas as pd

# Source: http://www.trumptwitterarchive.com/archive

THRESHOLD = .7
pos = 0
neg = 0
unc = 0
data = pd.read_csv('data/trump_tweets.csv')

def process_data():
    results = [None] * len(data)
    #print(data.head())

    for i, text in enumerate(data['text']):
        try:
            result = list(s.sentiment(text))
        except Exception as e:
            print(e)

        if result[1] < THRESHOLD:
            result[0] = 'UNCERTAIN'
        #print('Determined "{}" to be {} with {}% certainty.'.format(text, result[0], result[1]*100))
        if result[0] == 'pos':
            pos = pos + 1
        elif result[0] == 'neg':
            neg = neg + 1
        else:
            unc = unc + 1

        results[i] = result[0]
    print("Number of pos: ", pos)
    print("Number of neg: ", neg)
    print("Numer of unc: ", unc)
    print("Total: ", pos+neg+unc)
    print(data.head())

    return results


def write_data():
    data.to_csv('data/processed.csv')
    f = open('data/totals.txt', 'w')
    f.write('pos, ' + repr(pos) + '\n')
    f.write('neg, ' + repr(neg) + '\n')
    f.write('unc, ' + repr(unc) + '\n')
    f.close()


data['Sentiment'] = process_data()
write_data()