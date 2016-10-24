import requests
import urllib
from bs4 import BeautifulSoup
from urllib2 import HTTPError


def getImg(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
        'Cookie' : 'SUB=_2AkMgIqvPf8NhqwJRmP0WxW_hbI9xyQjEieLBAH7sJRMxHRl-yT9kqnYytRCu-1itQcfA2qxiAsLHnVbnDOM7Zg..; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWh3OjVACbiGOkCUdAqTjuh; SINAGLOBAL=3155680483237.433.1467890943151; login_sid_t=18b23f2ca7f9c5976e58979b3298b4c2; YF-Ugrow-G0=5b31332af1361e117ff29bb32e4d8439; YF-V5-G0=694581d81c495bd4b6d62b3ba4f9f1c8; YF-Page-G0=b9004652c3bb1711215bacc0d9b6f2b5; _s_tentry=news.ifeng.com; Apache=3651448589602.613.1477035244617; ULV=1477035245585:16:5:2:3651448589602.613.1477035244617:1476851999674; UOR=y.qq.com,widget.weibo.com,ucdok.com; WBStorage=86fb700cbf513258|undefined'
    }
    try:
        req = requests.get(url, headers=head)
        print req.text

        soup = BeautifulSoup(req.text, 'html.parser')
        img_url = soup.findall('img').get('src')  # img url
        return img_url

    except requests.ConnectionError as e:
        return None




def main():
    for num in (1,5):
        url = 'http://www.nianzhi.cc/weibo?p=' + str(num)

        img_list = getImg(url)

        for i in img_list:
            print i




if __name__ == '__main__':
    main()