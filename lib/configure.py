import os
import json

class BotConfig:
    def __init__(self):
        with open('config/config.json') as fjson:
            self.json_data = json.load(fjson)

    def url_list(self):
        return self.json_data["url_list"]

    @staticmethod
    def token():
        return os.environ['SLACK_BOT_TOKEN']
