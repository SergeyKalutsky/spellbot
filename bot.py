import logging
from words import get_word_data
from aiogram import Bot, Dispatcher, executor, types
from credentials import API_TOKEN
from database import t, sess
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button1 = KeyboardButton('/any')
button2 = KeyboardButton('/repeat')

markup = ReplyKeyboardMarkup().add(button1).add(button2)
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

word = None


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    global word
    word = None
    await message.reply('Choose a selection', reply_markup=markup)


@dp.message_handler(commands=['any'])
async def send_welcome(message: types.Message):
    global word
    defenition, word = get_word_data(repeate=False)
    await bot.send_audio(message.from_user.id, open("word.mp3", "rb"), performer="Word")
    await message.answer(defenition)
    await message.answer('_ '*len(word))


@dp.message_handler(commands=['repeat'])
async def send_welcome(message: types.Message):
    global word
    defenition, word = get_word_data(repeate=True)
    await bot.send_audio(message.from_user.id, open("word.mp3", "rb"), performer="Word")
    await message.answer(defenition)
    await message.answer('_ '*len(word))


@dp.message_handler(commands=['del'])
async def send_welcome(message: types.Message):
    word = message.get_args()
    sess.query(t.Words).filter(t.Words.word == word).delete()
    sess.commit()
    await message.reply(f'Word {word} has been deleted')


@dp.message_handler(commands=['add'])
async def send_welcome(message: types.Message):
    word = message.get_args()
    row = sess.query(t.Words).filter(t.Words.word == word).first()
    if row:
        await message.reply(f'Word {word} has already exists')
        return
    sess.add(t.Words(word=word, correct=0, wrong=0))
    sess.commit()
    await message.reply(f'Word {word} has been added')


@dp.message_handler()
async def echo(message: types.Message):
    global word
    if word is not None and word != message.text:
        row = sess.query(t.Words).filter(t.Words.word == word).first()
        row.wrong += 1
        sess.commit()
        await message.answer('Incorrect!')
        await message.answer(word)

    if word is not None and word == message.text:
        row = sess.query(t.Words).filter(t.Words.word == word).first()
        row.correct += 1
        sess.commit()
        await message.answer('Correct!')
    await message.reply('Choose a selection', reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
