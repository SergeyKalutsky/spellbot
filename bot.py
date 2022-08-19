import logging
from words import get_word_data
from aiogram import Bot, Dispatcher, executor, types
from credentials import API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

word = None

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    global word
    if word is not None and word != message.text:
        await message.answer('Неправильно!')
        await message.answer(word)
        
    defenition, word = get_word_data()
    await bot.send_audio(message.from_user.id, open("word.mp3", "rb"), performer="Word")
    await message.answer(defenition)
    await message.answer('_ '*len(word))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
