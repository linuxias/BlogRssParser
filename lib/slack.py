from slacker import Slacker
from lib.configure import BotConfig

class SlackUtil():
    def __init__(self):
        self.__slacker = Slacker(BotConfig.token())
        print(BotConfig.token())

    def post(self, user, title, link, pubDate):
        attatchment = [{
            "title" : "{}".format(title),
            "title_link" : "{}".format(link),
            "pub_date" : "{}".format(pubDate),
            }]

        self.__slacker.chat.post_message(channel = '#general', text = user, attachments = attatchment)

