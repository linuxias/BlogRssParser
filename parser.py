import sys
import feedparser
from slacker import Slacker
#from query import RssQuery

url_file = 'url_list'
token_file = 'token_file'

def get_url_list():
    url_list = []
    with open(url_file) as f:
        for data in f:
            url_list.append(data)
    return url_list

def get_token():
    token = ''
    try:
        with open(token_file) as f:
            token = f.readline()
    except BaseException as e:
        print(e)
        sys.exit()
    return token.strip()

def slacker_post(user, title, link):
    token = get_token()
    attatchment = [{
        "title" : "{}".format(title),
        "title_link" : "{}".format(link),

    }]
    slack = Slacker(token)
    slack.chat.post_message(channel = '#general', text = user, attachments = attatchment)

def main():
    url_list = get_url_list()

    for url in url_list:
        f = feedparser.parse(url)
        for var in f['entries']:
            slacker_post(var.get('author'), var.get('title'), var.get('link'))

if __name__=="__main__":
    main()
