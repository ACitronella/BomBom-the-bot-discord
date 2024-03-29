import os
from dotenv import load_dotenv
load_dotenv()

ACIVATE_MESSAGE = str(os.getenv("ACIVATE_MESSAGE"))
DISCORD_TOKEN = str(os.getenv("DISCORD_TOKEN"))
BOT_NOI_TOKEN = str(os.getenv("BOT_NOI_TOKEN"))
CHATBOT_STYLE = str(os.getenv("CHATBOT_STYLE"))
HEADERS = {"Authorization" : "Bearer " + BOT_NOI_TOKEN}
ALLOW_CHANNELS = [728666778229538869, 728621570435579954, 797403977297035264]
MONGO_URI = str(os.getenv("MONGO_URI"))
DATABASE_NAME = str(os.getenv("DATABASE_NAME"))
COLLECTION_NAME = str(os.getenv("COLLECTION_NAME"))