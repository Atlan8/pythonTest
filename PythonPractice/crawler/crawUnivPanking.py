import requests
from bs4 import BeautifulSoup
import bs4

# 获取静态页面
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status() # 抛出异常信息
        r.encoding = r.apparent_encoding # 改变编码
        return r.text
    except:
        return ''

# 提取HTML页面的静态信息
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])

# 打印输出
def printUnivList(ulist, num):
    # 第二个花括号里面的4代表使用format的第五个参数进行填充
    tplt = '{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}'
    print(tplt.format('排名', '学校名称', '省份', '总分', chr(12288))) # 表头,多余的空格使用中文空格代替，否则会出现不对齐的现象
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))

# 主函数
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 20 univs

main()