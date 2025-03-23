import random

def shuffle_words(words):
    return [''.join(random.sample(word, len(word))) for word in words]

words = ["apple", "banana", "cherry", "date", "elderberry"]
shuffled_words = shuffle_words(words)
print(shuffled_words)
