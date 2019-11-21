from urllib import request
from bs4 import BeautifulSoup
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
headers = {'User-Agent':user_agent}
url = 'https://www.ptt.cc/bbs/index.html'
req = request.Request(url = url,headers = headers)
res = request.urlopen(req)
#print(res.read().decode('utf-8'))

soup = BeautifulSoup(res.read().decode('utf-8'),'html.parser')
#print(soup)
# temp = soup.findAll('div', {'id': 'topbar'})
# print(temp[0].a.text)
# #print('https://www.ptt.cc/bbs' + temp[0].a['href'])

# tmp2 = soup.findAll('div',id = 'topbar')
# print(tmp2[0].a)
#
title = soup.findAll('a',class_ = 'board')
print()

for tmp_title in title:
    print(tmp_title.div.text)
    print('https://www.ptt.cc' + tmp_title['href'])