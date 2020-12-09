import discord
import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

class BOMTHEBOT(discord.Client):
    async def on_message(self, message):
        if message.author != self.user:
            print("ur mum") 
    async def on_connect(self):
        print('Hi')

bot = BOMTHEBOT()
bot.run(BOT_TOKEN)
