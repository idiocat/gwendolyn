from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
import utils.hp as hp

async def prop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hp.prop = update.message.text
    if hp.fonc == 'low' or hp.fonc == 'high':
        await update.message.reply_text("How many results do we need?")
        return 3
    elif hp.fonc == 'custom':
        await update.message.reply_text("In which range are we searching? (<number>-<number>)")
        return 1
    else:
        await update.message.reply_text("Wait, what are we doing here?")
        return ConversationHandler.END
