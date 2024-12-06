import logging
import requests
from requests.exceptions import RequestException
from ._base import Base

class Send(Base):

    def send_text(self, phone: str, text: str) -> str | None:
        try:
            with requests.Session() as session:
                url = f"{self.base_url}/waInstance{self.instance_id}/sendMessage/{self.api_token}"
                response = session.post(url, json={"chatId": self.phone_encode(phone), "message": text}, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if not data or not isinstance(data, dict):
                        return None
                    message_id = data.get("idMessage")
                    if message_id:
                        return message_id
                return None
        except RequestException as e:
                logging.error(f"RequestException: sendMessage: {e}")
                return None

    def send_poll(self, phone: str, text: str, options: list[str]) -> str | None:
        try:
            with requests.Session() as session:
                url = f"{self.base_url}/waInstance{self.instance_id}/sendPoll/{self.api_token}"
                response = session.post(url, json={"chatId": self.phone_encode(phone), "message": text[:255], "options": [{"optionName": option} for option in options[:12]]}, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if not data or not isinstance(data, dict):
                        return None
                    message_id = data.get("idMessage")
                    if message_id:
                        return message_id
                return None
        except RequestException as e:
                logging.error(f"RequestException: sendPoll: {e}")
                return None