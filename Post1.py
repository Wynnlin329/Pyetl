from urllib import parse
from urllib import request
import  requests
from bs4 import BeautifulSoup
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
headers={'User-Agent':user_agent}
#url='http://e2c87555.ngrok.io/hello_post'
url='http://e2c87555.ngrok.io/weather'
#post_data = {'username':'Allen'}
post_data = {'location':'基隆'}
res=requests.post(url,headers=headers,data=post_data)
# soup =BeautifulSoup(res.text,'html.parser')
# res_html=soup

print(res.text)