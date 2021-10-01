import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
import re

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_links(url):
    """
    Returns all image URLs on a single `url`
    """
    soup = bs(requests.get(url).content, "html.parser")

    #print(soup.find_all("a", {"id": "lnknav"}))
    urls = []
    for img in tqdm(soup.find_all("a", {"id": "lnknav"}), "Extracting images"):
        img_url = img.attrs.get("href")
        #print(img_url)
        match = re.search('actress', img_url)
        if match:
            img_url = "https://www.ragalahari.com" + img_url
            print(img_url)
            urls.append(img_url)
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
    return urls

def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """
    soup = bs(requests.get(url).content, "html.parser")


    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        print(img_url)
        match = re.search('t.jpg',img_url)
        if match:
            img_url = re.sub('t.jpg', '.jpg',img_url)
            urls.append(img_url)
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
    return urls

def main(url, path):
    # get all images
    imgs = get_all_images(url)
    print(imgs)
    #f = open('catherine','a')
    with open(path,'a') as f:
        for val in imgs:
            f.write(val)
            f.write('\n')
    # for img in imgs:
    #     # for each image, download it
    #     download(img, path)

def get_urls(url,num=None):
    lst = []
    if num is None:
        lst.append(url)
        return lst
    else:
        lst.append(url)
        for i in range(1,num):
            new_url = url.split('/')
            new_url.insert(-1,str(i))
            new_url = '/'.join(new_url)
            lst.append(new_url)
        return lst

if __name__ == '__main__':
    flag = True
    while True:
        user =input()
        limit = 100
        dat = user.split(' ')
        if len(dat) == 2:
            user = dat[0]
            page = int(dat[1])

        elif len(dat) ==3:
            user = dat[0]
            page = int(dat[1])
            flag = False
            limit = int(dat[2])
        else:
            user = dat[0]
            page =3


        print(user, page)
        lst_urls = []
        if flag:
            lst_urls = get_all_links(user)
        else:
            lst_urls = get_all_links(user)
            lst_urls = lst_urls[:limit]
        print(lst_urls)
        for u in lst_urls:
            urls =get_urls(
                u, page
            )
            for url in urls:
                main(url, "stored1/neha_shetty.txt")

        print ('DONE!!!!!!!!')


# link <no.of.pages>
# link <no.of.pages> <no.of.follow.links>