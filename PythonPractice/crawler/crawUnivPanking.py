import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status() # 抛出异常信息
        r.encoding = r.apparent_encoding # 改变编码
        return r.text
    except:
        return ''

def fillUnivList(ulist, html):
    pass

def printUnivList(ulist, num):
    print('Suc' + str(num))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 20 univs

main()