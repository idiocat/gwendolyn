import logging
from loader import application
from utils.set_commands import set_commands

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':
    set_commands(application)
    application.run_polling()