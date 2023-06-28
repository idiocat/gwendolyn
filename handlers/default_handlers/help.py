from telegram import Update
from telegram.ext import ContextTypes

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Here's a list of things you can do:\n\
\tget this list of things you can do by typing /help;\n\
\tpretend we never met before by typing /start;\n\
\tsay 'hello' or 'hi' to engage into an endless cycle of greetings exchange;\n\
\ttype /low, /high or /custom to search through database of exoplanets\n\
(data provided by PADC (http://voparis-tap-planeto.obspm.fr/)).")