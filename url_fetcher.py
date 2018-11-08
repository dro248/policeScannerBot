import requests
from bs4 import BeautifulSoup

class UrlFetcher:
    @staticmethod
    def fetch_url(url: str):
        try:
            # 'https://www.broadcastify.com/listen/feed/18656/web'
            r = requests.get(url)
            assert(r is not None)
            soup = BeautifulSoup(r.text, 'html.parser')
            audioTag = soup.find_all('audio')[0]
        except:
            return "bad request"
        return audioTag['src']
