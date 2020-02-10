import sys
import feedparser
from slacker import Slacker
import json
#from query import RssQuery

token_file = 'token_file'

class ParseConfig:
    def __init__(self):
        with open('config.json') as fjson:
            self.json_data = json.load(fjson)

    def url_list(self):
        return self.json_data["url_list"]

    def token(self):
        return str(self.json_data["token"])

def get_url_list():
    pc = ParseConfig()
    url_list = pc.url_list()
    return url_list

def slacker_post(user, title, link, pubDate):
    pc = ParseConfig()
    token = pc.token()
    attatchment = [{
        "title" : "{}".format(title),
        "title_link" : "{}".format(link),
        "pub_date" : "{}".format(pubDate),
    }]
    slack = Slacker(token)
    slack.chat.post_message(channel = '#general', text = user, attachments = attatchment)

def main():
    url_list = get_url_list()

    for url in url_list:
        f = feedparser.parse(url)
        for var in f['entries']:
            slacker_post(var.get('author'), var.get('title'), var.get('link'), var.get('pubDate'))

if __name__=="__main__":
    main()
