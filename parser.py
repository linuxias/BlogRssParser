import feedparser

url_list = { 'https://sonseungha.tistory.com/rss' }

def main():
    for url in url_list:
        feed = feedparser.parse(url)
        for item in feed['entries']:
            for var in item:
                print(var, ":" ,item[var])

if __name__=="__main__":
    main()