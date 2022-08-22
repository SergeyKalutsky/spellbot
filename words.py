import random
import requests
from gtts import gTTS
from database import t, sess

def get_word_data(repeate=False):
    if repeate:
        words = sess.query(t.Words.word).filter(t.Words.wrong > 0).all()
    else:
        words = sess.query(t.Words.word).all()
    words = [i[0] for i in words]
    indx = random.randint(0, len(words)-1)
    word = words[indx]
    res = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    defenition = res.json()[0]['meanings'][0]['definitions'][0]['definition']
    sound = gTTS(text=word, lang='en', slow=False)
    sound.save("word.mp3")
    return defenition, word
