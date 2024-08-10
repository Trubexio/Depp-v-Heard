 #pip install nltk matplotlib wordcloud numpy


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from _collections import defaultdict
import re
import pickle

# Download necessary NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

# Load the text file
with open('Dataset.txt' ,'r',  encoding="utf8") as file:
    text = file.read()

data = []
with open('Dataset.txt', 'r', encoding="utf8") as file:
    while True:
        # Get next line from file
        line = file.readline()
        # if line is empty
        # end of file is reached
        if not line:
            break
        result = re.search(r"\[(.*?)].*\[(.*?)]: (.*$)", line)
        if not result.group(3):
            continue
        data.append(result.group(3))

text = ' '.join(data)
# Tokenize the text
words = word_tokenize(text)

# Filter out stopwords and non-nouns
stop_words = set(stopwords.words('english'))
nouns = [word.title() for (word, pos) in pos_tag(words) if pos.startswith('N') and word.lower() not in stop_words]
cleaned_nouns = [re.sub(r'[^a-zA-Z0-9\s]+', ' ', noun) for noun in nouns if re.sub(r'[^a-zA-Z0-9\s]+', ' ', noun)]
frequency_table = defaultdict(int)
for word in cleaned_nouns: 
    frequency_table[word.title()] += 1

with open('word_freq_map.txt', 'wb') as handle:
  pickle.dump(frequency_table, handle)

# Create the word cloud
wordcloud = WordCloud(width=1920, height=1080, background_color='white',
                      collocations=False, stopwords=stop_words,min_word_length=6 , max_words=200).generate_from_frequencies(frequency_table)

wordcloud.to_file("world_cloud.png")
# Display the word cloud
plt.figure(figsize=(20, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()