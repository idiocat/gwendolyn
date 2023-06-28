from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text("Did you want something else?")
    return ConversationHandler.END
