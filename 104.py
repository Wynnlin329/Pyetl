import requests
from bs4  import BeautifulSoup
import os
import json
from urllib import request

user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

headers = {'User-Agent':user_agent}

url ='https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90&order=14&asc=0&page=1&mode=s&jobsource=2018indexpoc'
#url='https://www.104.com.tw/job/6bycm?jobsource=jolist_b_relevance'

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text,'html.parser')

title = soup.select('h2[class="b-tit"]')
#print(title[4].a['href'])

#print(title[4].text,title[4].a['href'].split())


# for title_all in range(4,len(title)):
#     print(title[title_all].text.split(),'\n','http://'+title[title_all].a['href'].replace('//',''))
#     #tmp_artical = [title_all].a['href'][21:26]

artical_url='https://www.104.com.tw/job/6qi7u?jobsource=hotjob_chr'
artical_res = requests.get(artical_url, headers=headers)
artical_soup = BeautifulSoup(artical_res.text,'html.parser')
artical_text = artical_soup.select('div[class="content"] p')
print(artical_text[0].text,'\n',artical_text[1].text)
print(artical_text)

# data = soup.select('p[class="job-list-item__info b-clearfix b-content"]')
# print(data)
# for i in data:
#      print(i.text)
#      print('--------------------------------')