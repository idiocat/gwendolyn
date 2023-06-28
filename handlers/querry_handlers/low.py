from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
import utils.hp as hp

async def low(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"What are we searching for? ({', '.join(hp.reply_keyboard[0])})",
                                    reply_markup=ReplyKeyboardMarkup(hp.reply_keyboard, one_time_keyboard=True))
    hp.fonc = 'low'
    return 0