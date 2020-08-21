from bs4 import BeautifulSoup as bs
import pandas as pd
import requests 
import re
 
url="https://news.tvbs.com.tw/local/1111922?from=Popular_txt_click"
headers={'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

html=requests.get(url,headers=headers)
html.encoding="utf-8"
soup=bs(html.text,"html.parser")


date=soup.find("div",class_="icon_time time leftBox2").text
date=date.replace(r"/","")
date=date[:8]


title=soup.find("h1",class_="margin_b20").text

source="tvbs"
content=soup.find("div",class_="h7 margin_b20").text

newsdict={}
newsdict["dict"]=date
newsdict["title"]=title
newsdict["source"]=source
newsdict["content"]=content

print(newsdict)