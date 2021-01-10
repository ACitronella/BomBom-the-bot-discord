import settings as ENV
import discord
from Services.chatbot import ChatBotService

class BOMTHEBOT(discord.Client):

    def __init__(self):
        super().__init__()
        self.voice_client = None

    async def connect_voice_channel(self, voice_channel):
        if voice_channel is not None:
            self.voice_client = await voice_channel.connect()

    async def on_message(self, message):
        # boolean
        is_not_self = message.author != self.user
        is_right_channel = message.channel.name in ENV.ALLOW_CHANNELS
        is_prefix_bom = message.content.startswith(ENV.ACIVATE_MESSAGE)
        if is_not_self and is_right_channel and is_prefix_bom:
            message_bot_got = message.content[len(ENV.ACIVATE_MESSAGE):]
            message_separated = message_bot_got.spilt()
            if message_separated[0] == "connect":
                await self.connect_voice_channel(message.author.voice.channel)
                
            elif message_separated[0] == "play":
                # if not connect connect voice channel
                if self.voice_client is None:
                    await self.connect_voice_channel(message.author.voice.channel)
                # use voice service here
                music = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("I:/OneDrive - kmutnb.ac.th/Music/ClariS/Gravity/01 Gravity.m4a"))
                self.voice_client.play(music)
                
            elif message_separated[0] == "exit":
                try:
                    await self.voice_client.disconnect()
                except AttributeError:
                    pass
                await message.channel.send("บาย")
                await self.logout()
                
            else:
                print("bot got a message:", message_bot_got, "from:", message.author.name)
                from_api = ChatBotService.botnoichitchat(message_bot_got) # call api from botnoi
                await message.channel.send(from_api)    


    async def on_connect(self):
        all_ch = self.get_all_channels()
        for channel in all_ch:
            if channel.name in ENV.ALLOW_CHANNELS:
                print("Bom found channel that he can speak.", channel.name)
                await channel.send("hi! im bom")

