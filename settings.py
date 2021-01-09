import os
from dotenv import load_dotenv
load_dotenv()

ACIVATE_MESSAGE = str(os.getenv("ACIVATE_MESSAGE"))
DISCORD_TOKEN = str(os.getenv("DISCORD_TOKEN"))
BOT_NOI_TOKEN = str(os.getenv("BOT_NOI_TOKEN"))
HEADERS = {"Authorization" : "Bearer " + BOT_NOI_TOKEN}
CHATBOT_STYLE = 25
ALLOW_CHANNELS = ["คุยกับbot-bombom"]
