import feedparser
from slacker import Slacker

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

def main():
    url_list = get_url_list()
    for url in url_list:
        f = feedparser.parse(url)
        for var in f:
            print(var)

    token = get_token()
    try:
        slack = Slacker(token)
        slack.chat.post_message('#general', 'Hello')
    except Exception as e:
        print('Wrong token : ', token)

if __name__=="__main__":
    main()
