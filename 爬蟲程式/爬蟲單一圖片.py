import requests
import os

saveDir='./images/'
if not os.path.isdir(saveDir):
    os.mkdir(saveDir)
    
url='https://assets.juksy.com/files/articles/87153/800x_100_w-5c4fcec51d548.jpg'
img=requests.get(url)
with open(saveDir+'Congestus_con.jpg','wb') as f:
    f.write(img.content)    