import requests
pic=requests.get("https://megapx-assets.dcard.tw/images/6aeea371-ef82-4259-97da-3869ce8f6a60/640.webp")
img2=pic.content
pic_out=open("img1.png",'wb')
pic_out.write(img2)
pic_out.close()