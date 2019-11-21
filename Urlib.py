from urllib import request
#user-agent，header使用者網頁資訊，為避免機器人
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
#User-Agent固定格式網頁才偵測的到
headers = {'User-Agent':user_agent}

url = 'https://www.ptt.cc/bbs/Salary/index.html'
#送出url與使用者資訊，向網頁請求，並將資料存入req
req = request.Request(url = url,headers = headers)
#打開回傳後的網頁存入res
res = request.urlopen(req)
#將網頁印出並編碼
print(res.read().decode('utf-8'))