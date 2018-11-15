import feedparser

url_file = 'url_list'

def get_url_list():
    url_list = []
    with open(url_file) as f:
        for data in f:
            url_list.append(data)

    return url_list

def main():
    url_list = get_url_list()
    for url in url_list:
        f = feedparser.parse(url)

if __name__=="__main__":
    main()