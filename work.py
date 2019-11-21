import requests
from bs4  import BeautifulSoup
import os
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'

headers = {'User-Agent':user_agent}
path = r'./res_gossiping_work'

if not os.path.exists(path):
    os.mkdir(path)

page = 39291
while page < 39293:
        url = 'https://www.ptt.cc/bbs/Gossiping/index%s.html'%(page)

        res=requests.get(url,headers=headers,cookies={'over18':'1'})
        soup = BeautifulSoup(res.text,'html.parser')

        title = soup.select('div[class="title"]')


       # page_url = 'https://www.ptt.cc/bbs/Gossiping/index%s.html'%(page)
        #page_res = requests.get(url, headers=headers, cookies={'over18': '1'})
        #soup_page = BeautifulSoup(page_res.text, 'html.parser')


        for title_all in range(len(title)):
            try:
                print( title[title_all].a.text,'\n','https://www.ptt.cc'+ title[title_all].a['href'])
                title_url ='https://www.ptt.cc'+ title[title_all].a['href']
            except AttributeError as e:
                print('---------------------------')
                print(e.args)
                print('---------------------------')
            article_res=requests.get(title_url,headers=headers,cookies={'over18':'1'})

            soup_article=BeautifulSoup(article_res.text,'html.parser')
            #print(soup_article.text
            title_content = soup_article.select('div[id="main-content"]')
            article_str = title_content[0].text.split('--')[0]
            #print(article_str)
            push_up = 0
            push_dw = 0
            #auther = ''
            score = 0
            #time = ''
            #title = ''

            push_info_list = soup_article.select('div[class="push"] span')
            for info in push_info_list:
                if '推' in info.text:
                    push_up +=1
                if '噓' in info.text:
                    push_dw +=1

            score = push_up - push_dw

            article_str += '--split--' + '\n'
            article_str += '推' + str(push_up) + '\n'
            article_str += '噓' + str(push_dw) + '\n'
            article_str += '分數' + str(score) + '\n'


            try:
                with open('%s/%s.txt'%(path,title[title_all].a.text.replace('?',' ')),'w',encoding='utf-8') as f:
                    f.write(article_str)
            except AttributeError as e:
                print(e.args)
            print(article_str)

        page +=1





