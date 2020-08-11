import sentiment_mod as s
import pandas as pd

THRESHOLD = .7

data = pd.read_csv('test.csv', names=['Id','Text'], header=None)
#print(data.head())

for text in data['Text']:
    result = list(s.sentiment(text))

    if result[1] < THRESHOLD:
        result[0] = 'UNCERTAIN'
    print('Determined "{}" to be {} with {}% certainty.'.format(text, result[0], result[1]*100))