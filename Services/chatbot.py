import json
import settings as ENV
from requests import request

class ChatBotService:

    @staticmethod
    def botnoichitchat(text:str, chatbot_style:str) -> str:
        url = f"https://openapi.botnoi.ai/service-api/botnoichitchat?keyword={text}&styleid={chatbot_style}&botname=น้องบอม"
        try:
            text_to_return = json.loads(request("GET", url, headers=ENV.HEADERS).text)["reply"]
        except KeyError as e:
            text_to_return = "Wait, im confusing"
            print(e)
        return text_to_return
