from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
import utils.hp as hp
import handlers.helping_handlers.output as output

async def amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hp.amount = update.message.text
    await update.message.reply_text("Cool. Let's see...")

    chat_id=update.effective_message.chat_id
    context.job_queue.run_once(output.output, .1, data=[hp.fonc, hp.prop, hp.amount, hp.search_range, hp.search_order],
                               chat_id=chat_id, name=str(chat_id))

    return ConversationHandler.END