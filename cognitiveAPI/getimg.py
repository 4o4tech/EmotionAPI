import requests
import urllib
from bs4 import BeautifulSoup
from urllib2 import HTTPError


def getImg(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'#,
        #'Cookie:'
    }
    try:
        req = requests.get(url, headers=head)
        req.encoding = 'gb18030'
        return req.text
    except requests.ConnectionError as error
        return None





def main():
    url = 'weibo.com'

    getImg(url)
if __name__ == '__main__':
    main()