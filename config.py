import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7495370078:AAGnQ62ns4kd3ScQyIsMsNyYbGm7rqU3Lb4")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20937630"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3290b11b9246bff1ff44f13e9c7ffb45")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
