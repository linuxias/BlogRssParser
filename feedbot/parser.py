import sys
import feedparser
from lib.configure import BotConfig
from lib.slack import SlackClient
from threading import Thread

class Bot(object):
    def __init__(self):
        self._config = BotConfig()
        self._slack = SlackClient()
        self._thread = Thread(target=self._routine)
        pass

    def _routine(self):
        for url in self._config.url_list():
            print(url)
            f = feedparser.parse(url)
            for var in list(f['entries'])[:self._config.nr_feed()]:
                self._slack.post(
                        var.get('author'),
                        var.get('title'),
                        var.get('link'),
                        var.get('pubDate')
                    )

    def run(self):
        self._thread.start()

def main():

    bot = Bot()
    bot.run()

if __name__=="__main__":
    main()
