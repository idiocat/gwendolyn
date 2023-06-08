import os
from dotenv import find_dotenv, load_dotenv

if find_dotenv():
    load_dotenv()
else:
    exit("NO .ENV")

BOT_TOKEN = os.getenv('BOT_TOKEN')
