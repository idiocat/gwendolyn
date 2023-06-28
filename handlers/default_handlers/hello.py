from random import randrange
from telegram import Update
from telegram.ext import ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):

    greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Oh hi', "What's up?", 'How are you doing?', 'How is it going?']
    await update.message.reply_text(greetings[randrange(len(greetings))])
