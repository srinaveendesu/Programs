import telebot

API_TOKEN = ''

import telegram

bot = telegram.Bot(token=API_TOKEN)

#print(bot.get_me())

#updates = bot.get_updates()
#print(updates)

# chat_id = bot.get_updates()[-1].message.chat_id
# print(chat_id)chat_id




import os
import time

cur_path = ''
def remote_send_photo():
    for dirpath,dirname,files in os.walk(r'''New folder\\New folder (8)'''):
        print(files,dirpath)
        for i,file in enumerate(files):
        #for i in range(0, len(files)):
            bot.send_photo(chat_id='-1001346702683', photo=open(os.path.join(dirpath,files[i]), 'rb'))
            time.sleep(2)
            print(i,'compressed file')

def remote_send_file():
    for dirpath, dirname, files in os.walk(r'''New folder\\New folder (8)'''):
        print(files, dirpath)
        for i, file in enumerate(files):
        #for i in range(0,10):
            bot.send_document(chat_id='-1001346702683', document=open(os.path.join(dirpath, files[i]), 'rb'))
            time.sleep(2)
            print(i,'file')

# start = time.time()
# remote_send_photo()
# end = time.time()
# print("Time consumed in working: ",end - start)

# use -100 as prefix for all codes

#bot.send_message(chat_id='-1001189087561', text="I'm sorry Dave I'm afraid I can't do that.")

#bot.send_photo(chat_id='-1001189087561', photo=open('actress_rezina_1.jpg', 'rb'))

#bot.send_document(chat_id='-1001189087561', document=open('actress_rezina_1.jpg', 'rb'))

#bot.send_photo(chat_id='-1001189087561', photo='link to upload')


import requests
from PIL import Image
# python2.x, use this instead
# from StringIO import StringIO
# for python3.x,
from io import StringIO, BytesIO
filename = 'neha_shetty.txt'
chat_id = '-100' +'1567716230'
page_no = 86

# dat5 1565805466
def send_url_photo(act,url, i=0):
    try:
        r = requests.get(url)
        image = Image.open(BytesIO(r.content))
        bio = BytesIO()
        bio.name = act
        image.save(bio, 'JPEG')
        bio.seek(0)
        bot.send_photo(chat_id=chat_id, photo=bio)
        r.close()
    except (requests.ConnectionError, requests.Timeout) as e:
        print(f'{i} failing try again1 - photo', e)
        send_url_photo(act, url, i)
    except Exception:
        print(f'{i} failing try again2 - photo')
        send_url_photo(act, url, i)

# need to add bot to channel before bot can send msgs
# working -1001426907042 dump_dat3
# working -1001346702683 dump_dat2
def send_url_file(act, url,i=0):
    try:
        r = requests.get(url)
        bot.send_document(chat_id=chat_id, document=BytesIO(r.content), filename=act)
        r.close()
    except (requests.ConnectionError,requests.Timeout ) as e:
        print(f'{i} failing try again - file', e)
        send_url_file(act,url, i)
    except Exception:
        print('failing try again - photo')
        send_url_file(act, url, i)

from collections import OrderedDict
od = OrderedDict()
def name():
    #data = None
    with open(filename,'r') as f:
        data = f.read()
        data = data.split('\n')

    for val in data:
        if val not in od:
            od[val] = 1
        else:
            od[val] = od[val]+ 1
    #print(len(od))
    # #for i, val in enumerate(data):
    # #927
    # for i in range(0, len(data)):
    #     act = data[i].split('/')[-1]
    #     start = time.time()
    #     send_url_photo(act, data[i])
    #     end = time.time()
    #     total_time = end - start
    #     print(i, 'compressed file', len(data) - i, total_time)
    #     if total_time <3:
    #         time.sleep(3 - total_time)

    data = list(od.keys())
    for i in range(page_no, len(data)):
        act = data[i].split('/')[-1]
        print(act,data[i])
        start = time.time()
        send_url_photo(act, data[i], i)
        end = time.time()
        total_time = end - start
        print(i, 'compressed file', len(data) - i, total_time, data[i])
        if total_time <3:
            time.sleep(3 - total_time)

    #for i in range(0, len(data)):
        #act = data[i].split('/')[-1]
        start = time.time()
        send_url_file(act, data[i], i)
        end = time.time()
        total_time = end - start
        print(i, 'file', len(data) - i, total_time)
        if total_time < 3:
            time.sleep(3 - total_time)



start = time.time()
name()
end = time.time()
print("Time consumed in working: ",end - start)


# Post an image from memory
# In this example, image is a PIL (or Pillow) Image object, but it works the same with all media types.
#
# from io import BytesIO
# bio = BytesIO()
# bio.name = 'image.jpeg'
# image.save(bio, 'JPEG')
# bio.seek(0)
# bot.send_photo(chat_id, photo=bio)

