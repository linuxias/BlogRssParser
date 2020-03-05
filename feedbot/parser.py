import sys
import feedparser
from lib.configure import BotConfig
from lib.slack import SlackUtil

def main():
    config = BotConfig()
    slack = SlackUtil()

    for url in config.url_list():
        print(url)
        f = feedparser.parse(url)
        for var in f['entries']:
            slack.post(
                    var.get('author'),
                    var.get('title'),
                    var.get('link'),
                    var.get('pubDate')
                )

if __name__=="__main__":
    main()
