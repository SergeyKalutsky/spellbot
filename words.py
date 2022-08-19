import pickle
import random
import requests
from gtts import gTTS

with open('words.pickle', 'rb') as f:
    words = pickle.load(f)

def get_word_data():
    indx = random.randint(0, len(words)-1)
    word = words[indx]
    res = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    defenition = res.json()[0]['meanings'][0]['definitions'][0]['definition']
    sound = gTTS(text=word, lang='en', slow=False)
    sound.save("word.mp3")
    return defenition, word
