import bs4.element
from bs4 import BeautifulSoup

import  requests

p_url = "https://www.ragalahari.com"

def all_thumbs(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    #print(soup)
    lst1 =[]
    lst2 =[]
    for link in soup.findAll('a'):
        try:
            if link.attrs['class'][0] == "galimg":
                #print(link.attrs['href'])
                lst1.append(link.attrs['href'])
        except:
            pass

    for link in soup.findAll('h2'):
        #link.contents[0].attrs['class'][0] == 'galleryname'
        try:
            if link.contents[0].attrs['id'] =='lnknav' and link.contents[0].attrs['class'][0] == 'galleryname':
                #print(link.contents[0].attrs['href'])
                lst2.append(link.contents[0].attrs['href'])
        except:
            pass
    print(len(lst2), len(lst1))
    return lst1, lst2



def jpg_getter(list_links):
    tmp_lst = []
    for link in list_links:
        url = p_url + link
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        #print(soup)
        try:
            if soup.findAll('td')[1].div.attrs['id'] == 'galdiv':
                for jp in soup.findAll('td')[1].contents[0].contents:
                    if isinstance(jp, bs4.element.Tag):
                        #print(jp)
                        tmp_lst.append(jp.img.attrs['src'].replace('t', ''))
                        #tmp_lst.append(jp.attrs['href'])
        except:
            pass

    return tmp_lst

def page_getter(link):
    url = p_url + link
    response = requests.get(url)
    tmp_lst = [link]
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    # soup.findAll('td')
    for page in soup.findAll('td'):
        try:
            if page['id'] == "pagingCell":
                for p in page.contents:
                    try:
                        if p.attrs['class'][0] == "otherPage":
                            if p.attrs['href'] not in tmp_lst:
                                tmp_lst.append(p.attrs['href'])
                            #print(p.attrs['href'])
                    except:
                        pass
        except:
            pass
    #print(tmp_lst)
    #for link in
    return tmp_lst

def file_builder(filename, url):
    ls1, lst2 = all_thumbs(url)
    f_list = []
    tot_jps = 0
    for link in lst2:
        p_list = page_getter(link)
        j_list = jpg_getter(p_list)
        print(len(p_list), len(j_list), link)
        tot_jps = tot_jps + len(j_list)
        f_list.extend(j_list)

    text = '\n'.join(f_list)
    with open(filename + f'_{tot_jps}.txt', 'w+') as f:
        f.write(text)
    print(tot_jps)


#"https://www.ragalahari.com/stars/profile/1289/hamsa-nandini.aspx"

file_builder(
    filename="shraddha_das",
    url="https://www.ragalahari.com/stars/profile/1651/shraddha-das.aspx"
)