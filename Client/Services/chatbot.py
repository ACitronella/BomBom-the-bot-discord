import json
import settings as ENV
from requests import request

class ChatBotService:

    @staticmethod
    def botnoichitchat(text):
        url = f"https://openapi.botnoi.ai/service-api/botnoichitchat?keyword={text}&styleid={ENV.CHATBOT_STYLE}&botname=น้องบอม"
        try:
            text_to_return = json.loads(request("GET", url, headers=ENV.HEADERS).text)["reply"]
        except Exception as e:
            text_to_return = "แปป กำลังเอ๋อ"
            print(e)
        return text_to_return
