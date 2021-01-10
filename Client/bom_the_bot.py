import settings as ENV
import discord
from Services.chatbot import ChatBotService

class BOMTHEBOT(discord.Client):

    async def on_message(self, message):
        # boolean
        is_not_self = message.author != self.user
        is_right_channel = message.channel.name in ENV.ALLOW_CHANNELS
        is_prefix_bom = message.content.startswith(ENV.ACIVATE_MESSAGE)
        if not (is_not_self and is_right_channel and is_prefix_bom):
            return

        message_bot_got = message.content[len(ENV.ACIVATE_MESSAGE):]
        if message_bot_got == "exit":
            await message.channel.send("บาย")
            await self.close()

        print("bot got a message:", message_bot_got, "from:", message.author.name)
        from_api = ChatBotService.botnoichitchat(message_bot_got) # call api from botnoi
        await message.channel.send(from_api)
        

    async def on_connect(self):
        all_ch = self.get_all_channels()
        for channel in all_ch:
            
            if channel.name in ENV.ALLOW_CHANNELS:
                print("Bom found channel that he can speak.", channel.name)
                await channel.send("hi! im bom")

