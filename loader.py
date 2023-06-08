from telegram.ext import ApplicationBuilder
from config_data import config


application = ApplicationBuilder().token(config.BOT_TOKEN).build()
