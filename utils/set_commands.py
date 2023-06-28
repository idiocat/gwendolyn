import re
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, filters
from handlers.default_handlers import *
from handlers.querry_handlers import *
from handlers.helping_handlers import *


def set_commands(application):
    application.add_handler(CommandHandler('start', start.start))
    application.add_handler(CommandHandler('help', help.help))

    application.add_handler(ConversationHandler(
        entry_points=[CommandHandler('low', low.low), CommandHandler('high', high.high), CommandHandler('custom', custom.custom)],
        states={
            0: [MessageHandler(filters.Regex(r'^(mass|radius|semi_major_axis|period|eccentricity|discovered|ra|dec)$'), prop.prop)],
            1: [MessageHandler(filters.Regex(r'\d+-\d+'), range.range)],
            3: [MessageHandler(filters.Regex(r'\d+'), amount.amount)],
        },
        fallbacks=[CommandHandler("cancel", cancel.cancel)],
    ))


    application.add_handler(MessageHandler(filters.Regex(re.compile(r'hello|hi|hey', re.IGNORECASE)), hello.hello))