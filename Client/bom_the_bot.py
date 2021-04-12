from DatabaseConnector.Database import DatabaseService
from Services.chatbot import ChatBotService

import settings as ENV
import discord



class BOMTHEBOT(discord.Client):

    def __init__(self, db: DatabaseService):
        super().__init__()
        self.voice_client = None
        self.db_connected = db

    async def connect_voice_channel(self, voice_channel):
        if voice_channel is not None:
            self.voice_client = await voice_channel.connect()
    
    # message: discord.message.Message
    async def on_message(self, message: discord.message.Message):

        is_not_self = message.author != self.user
        is_right_channel = message.channel.id in ENV.ALLOW_CHANNELS
        is_prefix_bom = message.content.startswith(ENV.ACIVATE_MESSAGE)
        
        if is_not_self and is_right_channel and is_prefix_bom:
            message_bot_got = message.content[len(ENV.ACIVATE_MESSAGE):]
            message_separated = message_bot_got.split()
            if message_separated[0].lower() == "connect":
                await self.connect_voice_channel(message.author.voice.channel)
                
            elif message_separated[0].lower() == "play":
                # if not connect connect voice channel
                if self.voice_client is None:
                    await self.connect_voice_channel(message.author.voice.channel)
                # use voice service here
                music = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("I:/OneDrive - kmutnb.ac.th/Music/ClariS/Gravity/01 Gravity.m4a"))
                self.voice_client.play(music)
                
            elif message_separated[0].lower() == "exit":
                try:
                    await self.voice_client.disconnect()
                except AttributeError:
                    pass
                self.db_connected.close_connection()
                await message.channel.send("Bye!~")
                await self.logout()
                
            elif message_separated[0].lower() == "chat":
                # using chatbot service here
                try:
                    print("bot got a message:", message_bot_got, "from:", message.author, "channel:", message.channel.name)
                    from_api = ChatBotService.botnoichitchat(message_bot_got[4:], ENV.CHATBOT_STYLE)
                    await message.channel.send(from_api)
                except IndexError:
                    print("IndexError: something weird happend")

            # rewrite this later
            # elif message_separated[0].lower() == "addchannel":
            #     ENV.ALLOW_CHANNELS.append(message.channel.id)

        elif is_not_self and is_right_channel:
            print("Bom senses your line:", message.author, message.channel.name, message.content)
            self.db_connected.insert_one(message)



    async def on_connect(self):
        for channel in self.get_all_channels():
            print("channel: ", channel.name)
            if channel.id in ENV.ALLOW_CHANNELS:
                print("Bom found channel that he can speak.", channel.name)


