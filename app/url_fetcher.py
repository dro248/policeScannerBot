import requests
#! /usr/bin/python3

from bs4 import BeautifulSoup
import sys

class UrlFetcher:
    @staticmethod
    def fetch_url(page_url: str):
        """
        The fetch_url method makes a request for the page_url. 
        If that page contains an <audio> tag, the method returns the link in the <audio> tag's src attribute
        (e.g. <audio src="http://a.source.url.mp3">).
        Otherwise, it returns the string "bad request".

        :page_url: a url which should point to an html page containing an <audio> tag.
        :return: src_url | "bad request"
        """
        try:
            # 'https://www.broadcastify.com/listen/feed/18656/web'
            r = requests.get(page_url)
            assert(r is not None)
            soup = BeautifulSoup(r.text, 'html.parser')
            audioTag = soup.find_all('audio')[0]
            return audioTag['src']
        except:
            return "bad request"
        

if __name__ == '__main__':
    if(len(sys.argv) > 0):
        url = sys.argv[1]
        print(UrlFetcher.fetch_url(url))
    else:
        print("Error: Not enough arguments. Make sure to include a url when calling from the command line.")
