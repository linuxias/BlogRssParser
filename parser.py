import feedparser
from slacker import Slacker
from query import RssQuery

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
    with open(token_file) as f:
        token = f.readline()
    return token.strip()

def slacker_post():
    token = get_token()
    attatchment = [{
        "title" : "title test",
        "title_link" : "https://sonseungha.tistory.com"
    }]
    slack = Slacker(token)
    slack.chat.post_message(channel='#general', text='New article', attachments = attatchment)

def main():
    url_list = get_url_list()

    for url in url_list:
        f = feedparser.parse(url)
        for var in f:
            print(var)

    slacker_post()

if __name__=="__main__":
    main()
