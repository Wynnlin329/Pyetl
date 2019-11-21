import requests
from bs4 import BeautifulSoup
import json
from urllib import request
import os

# user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
# headers={'User-Agent':user_agent}
# url ='https://www.dcard.tw/_api/forums/photography/posts?popular=false&limit=30&before=232063592'
# res=requests.get(url,headers=headers)
# soup=BeautifulSoup(res.text,'html.parser')
# print(soup)
photo_path = r'./photo'
if not os.path.exists(photo_path):
    os.mkdir(photo_path)

with open('./json2','r',encoding='utf-8') as f:
    tmp_json = f.read()
#print(tmp_json)

js_dict = json.loads(tmp_json)
# for i in js_dict:
# #     print(i)
for i in js_dict:
    print(i['title'])
    print('https://www.dcard.tw/f/photography/p/'+str(i['id']))
    for n,j in enumerate(i['mediaMeta']):
        photo_url = j['url']
        print(photo_url)
        request.urlretrieve(photo_url,photo_path + '/%s%s.jpg'%(i['title'].replace("?","-").replace("？","-"),n))