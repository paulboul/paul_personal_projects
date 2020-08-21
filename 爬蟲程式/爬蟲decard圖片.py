##########imports##########
import requests
import json
import os
###########################
#解析JSON


def Data_to_Dcard(infor_json, index):
    Dcard_Json = {
        'id': 0,
        'title': 'title',
        'gender': 'M',
        'topics': [],
        'url': '',
        'likeCount': 0,
        'commentCount': 0,
        'media': [],
        'mediaCount': 0
    }

    Dcard_Json['id'] = int(infor_json['id'])
    Dcard_Json['title'] = str(infor_json['title'])
    Dcard_Json['gender'] = str(infor_json['gender'])
    Dcard_Json['topics'] = infor_json['topics']
    Dcard_Json['url'] = 'https://www.dcard.tw/f/' + \
        forums + '/p/' + str(infor_json['id'])
    Dcard_Json['likeCount'] = int(infor_json['likeCount'])
    Dcard_Json['commentCount'] = int(infor_json['commentCount'])
    Dcard_Json['media'] = infor_json['media']
    Dcard_Json['mediaCount'] = int(len(infor_json['media']))

    print("{:3d} 編號：{}｜網址：{}｜性別：{}｜讚數：{:5d}｜圖片數量：{}｜標題：{}".format(
        index + 1,
        str(infor_json['id']),
        str(Dcard_Json['url']),
        str(Dcard_Json['gender']),
        Dcard_Json['likeCount'],
        Dcard_Json['mediaCount'],
        str(Dcard_Json['title'])
    )
    )

    return Dcard_Json
###########################
#寫入JSON


def Data_inject(datas):
    Dcard_infors = []
    for index, data in enumerate(datas):
        Dcard_infors.append([])
        Dcard_infors[index] = Data_to_Dcard(data, index)
    return Dcard_infors
###########################
#算性別人數、讚數、圖片數


def Compute_sex(datas):
    Male = 0  # 男
    Male_l = 0  # 男
    Male_p = 0  # 男

    Female = 0  # 女
    Female_l = 0  # 女
    Female_p = 0  # 女
    for sex in datas:
        if sex['gender'] == 'M':
            Male += 1
            Male_l += sex['likeCount']
            Male_p += sex['mediaCount']
        elif sex['gender'] == 'F':
            Female += 1
            Female_l += sex['likeCount']
            Female_p += sex['mediaCount']

    done = [[Male, Male_l, Male_p], [Female, Female_l, Female_p]]

    print("男性=>發文篇數：{:2d}｜讚數：{:2d}｜圖片數：{:2d}\n女性=>發文篇數：{:2d}｜讚數：{:2d}｜圖片數：{:2d}\n".format(
        done[0][0], done[0][1], done[0][2],
        done[1][0], done[1][1], done[1][2]
    )
    )
    return done
###########################
#下載圖片


def download_image(datas):
    folder_path = './dacad/' + forums + '/'

    if (os.path.exists(folder_path) == False):  # 判斷主資料夾是否存在
        os.makedirs(folder_path)  # Create folder

    for images in datas:
        if images['mediaCount'] > 0:
            for index, image_url in enumerate(images['media']):
                image = requests.get(str(image_url['url']))  # for content
                img_name = folder_path + str(images['title']).replace('\\', '').replace('/', '').replace(':', '').replace(
                    '*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '') + '/'
                if (os.path.exists(img_name) == False):  # 判斷副資料夾是否存在
                    os.makedirs(img_name)  # Create folder
                with open(img_name + str(index + 1) + '.png', 'wb') as file:  # 以byte的形式將圖片數據寫入
                    file.write(image.content)
                    file.flush()
                file.close()  # close file
                print("完成：{}，第 {} 張照片，剩餘 {} 張需要下載".format(
                    images['title'], index + 1, images['mediaCount'] - index - 1))
                #http://dangerlover9403.pixnet.net/blog/post/207823890-%5Bpython%5D-day14---python-%E5%BE%9E%E7%B6%B2%E8%B7%AF%E6%8A%93%E5%9C%96%E7%89%87
            print("##########完成", images['title'], "##########\n")
    print("圖片下載完成...")


###########################
#for_dcard
Dcard_Api = {
    'popular': 'false',  # 熱門
    'limit': '30'  # 顯示文章篇數，最多100篇
}

url = 'https://www.dcard.tw/_api/forums/'
forums = 'sex'  # 板塊名稱

#init
Dcard = requests.get(url + forums + '/posts?', params=Dcard_Api)
Dcard_to_Json = json.loads(Dcard.text)
###########################
#1
Dcard_format = Data_inject(Dcard_to_Json)
#show male and female infor
print("##########數據分析##########")
Compute_sex(Dcard_format)
#download images
print("##########圖片下載##########")
download_image(Dcard_format)
