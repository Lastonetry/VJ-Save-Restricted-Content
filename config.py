import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "14766829"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "cfaca926290f395a7404927ccb88422d")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://tabolo8539:0evqZDV4fC5fD17c@cluster0.cw8zxus.mongodb.net/?retryWrites=true&w=majority")
