import re
from telegram.ext import CommandHandler, MessageHandler, filters
from handlers.default_handlers import *


def set_commands(application):
    application.add_handler(CommandHandler('start', start.start))
    application.add_handler(CommandHandler('help', help.help))
    application.add_handler(MessageHandler(filters.Regex(re.compile(r'hello|hi|hey', re.IGNORECASE)), hello.hello))