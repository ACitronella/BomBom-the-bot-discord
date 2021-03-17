import os
from dotenv import load_dotenv
load_dotenv()

ACIVATE_MESSAGE = str(os.getenv("ACIVATE_MESSAGE"))
DISCORD_TOKEN = str(os.getenv("DISCORD_TOKEN"))
BOT_NOI_TOKEN = str(os.getenv("BOT_NOI_TOKEN"))
CHATBOT_STYLE = str(os.getenv("CHATBOT_STYLE"))
HEADERS = {"Authorization" : "Bearer " + BOT_NOI_TOKEN}
ALLOW_CHANNELS = ["คุยกับbot-bombom"]
MONGO_URI = str(os.getenv("MONGO_URI"))
DATABASE_NAME = str(os.getenv("DATABASE_NAME"))
COLLECTION_NAME = str(os.getenv("COLLECTION_NAME"))