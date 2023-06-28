from telegram import Update
from telegram.ext import ContextTypes
import utils.hp as hp

async def range(update: Update, context: ContextTypes.DEFAULT_TYPE):
    search_range = update.message.text
    search_start, search_end = search_range.split('-')
    if int(search_start) > int(search_end):
        hp.search_range = f"{search_end}-{search_start}"
        hp.search_order = 'DESC'
    else:
        hp.search_range = f"{search_start}-{search_end}"
        hp.search_order = 'ASC'

    await update.message.reply_text("How many results do we need?")
    return 3

    