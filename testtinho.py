from pycounts.pycounts import count_words
from pycounts.plotting import plot_words
import matplotlib.pyplot as plt

word_counts = count_words("zen.txt")
plot_words(word_counts, 12)
plt.show()






