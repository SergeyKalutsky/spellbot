from tqdm import tqdm
import pickle
from database import sess, t

with open('words.pickle', 'rb') as f:
    words = pickle.load(f)

for word in tqdm(words):
    sess.add(t.Words(word=word, correct=0))
sess.commit()