import logging
import requests
from requests.exceptions import RequestException
from ._config import Config

class API(Config):

    def call_instance_api(self, method: str, json: dict | None = None) -> dict | None:
        try:
            with requests.Session() as session:
                url = f"{self.base_url}/waInstance{self.instance_id}/{method}/{self.api_token}"
                response = session.post(url, json=json, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if data and isinstance(data, dict):
                        return data
        except RequestException as e:
                logging.error(f"RequestException: {method}: {e}")