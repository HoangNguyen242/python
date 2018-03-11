# import
import io
import requests 
import bs4
import json
import time
import codecs

from urlparse import urljoin 
##from urllib.parse import urljoin

# Default value
SOURCE_URL = 'http://vietnamnet.vn/vn/cong-nghe/'
TARGET_DIRECTORY = '/root/Python/Crawl-python/results/'
LIST_POST = []

# functions define
def get_content_post(CONTENT_URL):
    """Crawl du lieu bai viet"""
    data = {}
    r = requests.get(CONTENT_URL)
    if r.ok:
        s = bs4.BeautifulSoup(r.content, 'lxml')        
        title = s.select_one('h1.title').next
        data['title'] = title.string
        sub_title = s.select_one('#ArticleContent > p > span')
        data['sub_title'] = sub_title.string
        content = s.select_one('#ArticleContent')
        data['content'] = content.prettify() if content else ''
        time = s.select_one('.ArticleDate').next
        data['time'] = time
        data['link'] = CONTENT_URL
        
    else: 
        print("khong truy cap duoc")
    return data 

def get_list_post():
    #LIST_POST = []
    r = requests.get(SOURCE_URL)
    if r.ok:
        s = bs4.BeautifulSoup(r.content, 'lxml')        
        list_obj = s.select('.item.clearfix.dotter > a')
        for obj in list_obj:           
            link_unjoin = obj.attrs['href'] # lay duong dan (thieu)
            link_obj = urljoin(SOURCE_URL, link_unjoin) # lay duong dan day du
            LIST_POST.append(link_obj)
            print(link_obj)            
    else: 
        print("khong truy cap duoc")
    

def crawl_content_of_list_post():
    for link_post in LIST_POST:
        print link_post

def get_list_link():
    LIST_POST = []
    r = requests.get(SOURCE_URL)
    if r.ok:
        s = bs4.BeautifulSoup(r.content, 'lxml')        
        list_obj = s.select('.item.clearfix.dotter > a')
        for obj in list_obj:
            time.sleep(1)  
            link_unjoin = obj.attrs['href'] # lay duong dan (thieu)
            link_obj = urljoin(SOURCE_URL, link_unjoin) # lay duong dan day du
            print(link_obj)
            data_to_json=get_content_post(link_obj) # lay du lieu bai viet
            print(convert_json_create_file(data_to_json, get_file_name(link_unjoin))) # tao file
    else: 
        print("khong truy cap duoc")
    return LIST_POST


def get_file_name(link_target):
    """ Tao duong dan File Name"""
    process_name_file_json = link_target.split("/")
    name_file_json = process_name_file_json[4].split(".")
    file_name = TARGET_DIRECTORY + name_file_json[0] + '.json'
    return file_name

def convert_json_create_file(json_data, file_name):
    """ Convert Json va tao file"""
    f = codecs.open(file_name, encoding='utf8', mode='w')
    json.dump(json_data, f, ensure_ascii=False, indent=2)
    return "done"

# main component
def main():
    #print(get_list_link())
    get_list_post()
    crawl_content_of_list_post()
    #data_to_json=get_content_post('http://vietnamnet.vn/vn/cong-nghe/tin-cong-nghe/samsung-dang-nam-giu-cong-nghe-sac-pin-dot-pha-434821.html')
    #print(data_to_json)
    #f = codecs.open('/root/Python/Crawl-python/data.json',encoding='utf8', mode='w')
    #json.dump(data_to_json, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()