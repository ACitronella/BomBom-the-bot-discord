import settings as ENV
from Client.bom_the_bot import BOMTHEBOT
import logging

# print("ACIVATE_MESSAGE =", ENV.ACIVATE_MESSAGE)
# print("ALLOW_CHANNELS =",ENV.ALLOW_CHANNELS)
# print("BOT_NOI_TOKEN =", ENV.BOT_NOI_TOKEN)
# print("DISCORD_TOKEN =", ENV.DISCORD_TOKEN)
# print("CHATBOT_STYLE =", ENV.CHATBOT_STYLE)
# print("HEADERS =", ENV.HEADERS)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = BOMTHEBOT()
bot.run(ENV.DISCORD_TOKEN)
