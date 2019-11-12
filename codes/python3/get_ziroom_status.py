#python3
import requests
import time
from lxml import etree
import pync
import random
# import pygame

url = 'http://www.ziroom.com/x/765858926.html'

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()



def get_status():
    response = requests.get(url, headers=headers)

    html = etree.HTML(response.content)
    status = html.xpath('//h1[@class="Z_name"]/i/@class')[0].split(' ')[1]
    if status == 'iconicon_release':
        print('待释放')
    else:
        print('!' * 10 + '\n')
        pync.notify('自如房子释放啦！')
        # file = r'/Users/lsun/Music/test.mp3'
        # pygame.mixer.init()
        # pygame.mixer.music.load(file)
        # pygame.mixer.music.play()
        time.sleep(60)


cnt = 0
while True:
    print('第 %d 次尝试 ' % cnt)
    get_status()
    cnt = cnt + 1
    t = random.randint(1, 100)
    print('Sleep %d' % t)
    time.sleep(t)
