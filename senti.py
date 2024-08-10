# -*- coding: utf-8 -*-
import re
# Analyze the sentiments of the comment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# For visualization
import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv("dataset.csv", sep=',', escapechar='%', encoding='utf-8')


polarity_list = []
sentiment_list = []

for index, row in df.iterrows():
    try:
        comment = row[2].lower().strip()
        sentiment_object = SentimentIntensityAnalyzer()
        sentiment_dict = sentiment_object.polarity_scores(comment)
        polarity = sentiment_dict['compound']
        sentiment = '-'
        if polarity > 0.05:
            sentiment = 'p'
        elif polarity < -0.05:
            sentiment = 'n'
        polarity_list.append(polarity)
        sentiment_list.append(sentiment)
    except IndexError:
        print(row)
        polarity_list.append(0)
        sentiment_list.append('-')
        raise

print('Total:',df.count())
print('polarity:',len(polarity_list))
print('sentiment:',len(sentiment_list))

new_data = {'polarity': polarity_list, 'sentiment': sentiment_list}
df = df.assign(**new_data)

df.to_csv('Dataset1senti.csv', sep=',', encoding='utf-8',  escapechar='%', index=False, header=True)


avg_polarity = sum(polarity_list) / len(polarity_list)
print("Average Polarity:", avg_polarity)
if avg_polarity > 0.05:
    print("The Video has got a Positive response")
elif avg_polarity < -0.05:
    print("The Video has got a Negative response")
else:
    print("The Video has got a Neutral response")

