from telegram import Update
from telegram.ext import ContextTypes

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here's a list of things you can do:\n\
\tget this list of things you can do by typing /help;\n\
\tpretend we never met before by typing /start;\n\
\tsay 'hello' or 'hi' to engage into an endless cycle of greetings exchange.")