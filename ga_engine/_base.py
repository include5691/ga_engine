import os

class Base:

    base_url = os.getenv("GREENAPI_BASE_URL")

    @staticmethod
    def phone_encode(phone: str) -> str:
        return str(phone) + "@c.us"

    @staticmethod
    def phone_decode(chatId: str) -> str:
        return chatId.split("@")[0]

    def __init__(self, instance_id: str, api_token: str):
        self.instance_id = instance_id
        self.api_token = api_token