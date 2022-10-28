import matplotlib.pyplot as plt

def plot_words(word_counts, n):
    """Plot a bar chart with the word counts"""
    top_n_words = word_counts.most_common(n)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation = 45)
    plt.xlabel("Word")
    plt.ylabel("Count")
    return fig
