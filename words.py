import pickle

with open('words.pickle', 'rb') as f:
    words = pickle.load(f)

print(words)