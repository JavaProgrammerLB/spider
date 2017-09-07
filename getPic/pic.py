#encoding=utf-8
import urllib.request
import re
import random
import os

user_agent = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"]

def getHtml(url):
    req = urllib.request.Request(url, headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    page = urllib.request.urlopen(req)
    html = page.read()
    return html

def getImg(html):
    reg = r'(?<=<img src=)"([^"]+\.jpg)"'
    imgre = re.compile(reg)
    html = html.decode('utf-8')  # python3
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        print(imgurl)
       #urllib.request.urlretrieve(request,'%s.jpg' % x)
        req = urllib.request.Request(imgurl, headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
            'Connection':'keep-alive',
            'Host':'thumb.comic.naver.net',
            'Upgrade-Insecure-Requests':1,
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
        })

        with urllib.request.urlopen(req) as d:
            pic = d.read()
            path = os.getcwd() + os.path.sep +  "{}.jpg".format(x)
            File = open(path, 'wb')
            File.write(pic)
            File.close
        x+=1

html = getHtml("http://comic.naver.com/webtoon/detail.nhn?titleId=644180&no=984&weekday=mon")
getImg(html)

