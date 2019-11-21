import requests

import urllib.request

from bs4 import BeautifulSoup

import os

import time

url = 'https://love708694.pixnet.net/blog/post/119990805'

photolimit = 999

link = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

response = requests.get(url, headers=headers)  # 使用header避免訪問受到限制

soup = BeautifulSoup(response.content, 'html.parser')

items = soup.find_all('img')

folder_path = './photo/'

# if (os.path.exists(folder_path) == False): #判斷資料夾是否存在

#     os.makedirs(folder_path) #Create folder

# print(type(items))


for index, item in enumerate(items):
    try:

        if (index < photolimit):
            html = requests.get(item['src'])  # use 'get' to get photo link path , requests = send request

            img_name = folder_path + str(index + 1) + '.jpg'

            #         link.append(html)
            print(item['src'])

            print(html)

            print(img_name)
            link
            with open(img_name, 'wb') as file:  # 以byte的形式將圖片數據寫入

                file.write(html.content)

            print('第 %d 張' % (index + 1))

            time.sleep(2)

    except:
        pass

print('Done')