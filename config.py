import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7708732142:AAGdBAebaZZQbGxvH30hrutNedCMQ2_TdpY")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22836334"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "072b12319aa045abd8710bd92eafbf4b")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ketbenduc:cXv6MNsgWtRZbLiJ@cluster0.cjyln.mongodb.net/?retryWrites=true&w=majority")
