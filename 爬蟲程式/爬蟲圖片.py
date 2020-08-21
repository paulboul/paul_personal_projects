import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import os



def get_google_images_links(searchTerm,download_folder):
    searchUrl="https://www.google.com/search?q=%E5%A4%A7%E5%A5%B6%E5%9C%96%E7%89%87%E7%B6%B2%E7%AB%99&hl=zh-TW&sxsrf=ALeKk01oQ62rK1hc46Zq0y08g_LFqELJbA:1593339537159&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi9mfmopKTqAhUHx4sBHVLnB0MQ_AUoAXoECAsQAw&biw=1536&bih=754"+searchTerm
   # searchUrl="https://www.google.com/search?q=%E5%8F%B0%E7%81%A3%E5%A5%B3%E7%A5%9E%E5%9C%96%E7%89%87%E7%B6%B2%E7%AB%99&sxsrf=ALeKk02fOrK5m4736VRXoWmqONAkdghhTA:1593335059527&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjxruzRk6TqAhXpDaYKHYteBIcQ_AUoAXoECAsQAw".format(searchTerm)
    LEN=len(searchUrl)
    print('ROOT='+str(LEN))
    i=0
    slash=0
    while i<LEN:
        if(searchUrl[i]=='/'):
            slash+=1
        if slash==2:
            roothttp=searchUrl[0:i+1]
        i+=1
        
    print('length='+str(roothttp))
    data=requests.get(searchUrl).text
    soup=BeautifulSoup(data,'html.parser')
    
    img_tags=soup.find_all('img')
    
    j=1
    for img in img_tags:
        if(img['src'].startswith("http")):
            WriteFilename=download_folder+'/'+searchTerm+str(j)+'.jpg'
            urllib.request.urlretrieve(img['src'],WriteFilename)
            print("\n"+str(img['src']))
        j+=1
            
download_folder="./downloads"
if not os.path.exists(download_folder):
    os.makedirs(download_folder)
    
get_google_images_links('beauty',download_folder)


