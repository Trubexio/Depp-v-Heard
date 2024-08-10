import matplotlib.pyplot as plt

import pandas as pd


def gen_figs(prefix, positive_count, negative_count, neutral_count):
    # labels and data for Bar chart
    labels = ['Positive', 'Negative', 'Neutral']
    comment_counts = [positive_count, negative_count, neutral_count]

    # Creating bar chart
    plt.bar(labels, comment_counts, color=['blue', 'red', 'grey'])

    # Adding labels and title to the plot
    plt.xlabel('Sentiment')
    plt.ylabel('Comment Count')
    plt.title('Sentiment Analysis of Comments')

    # Displaying the chart
    plt.savefig(prefix + '-bar.png')

    plt.clf()

    # labels and data for Bar chart
    labels = ['Positive', 'Negative', 'Neutral']
    comment_counts = [positive_count, negative_count, neutral_count]

    plt.figure(figsize=(10, 6))  # setting size

    # plotting pie chart
    plt.pie(comment_counts, labels=labels)

    # Displaying Pie Chart
    plt.savefig(prefix + '-pie.png')
    plt.clf()


def gen_for(the_column, df):
    grouped = df.groupby([the_column, 'sentiment'])
    result = grouped['comment'].count()
    print(result)
    positive_count = result[1, 'p']
    negative_count = result[1, 'n']
    neutral_count = result[1, '-']
    gen_figs(the_column, positive_count, negative_count, neutral_count)


def gen_overall(df):
    grouped = df.groupby(['sentiment'])
    result = grouped['comment'].count()
    print(result)
    positive_count = result['p']
    negative_count = result['n']
    neutral_count = result['-']
    gen_figs('all', positive_count, negative_count, neutral_count)


df = pd.read_csv("datasetsenti.csv", sep=',', escapechar='%', encoding='utf-8')
gen_overall(df)
gen_for('amber', df)
gen_for('depp', df)
