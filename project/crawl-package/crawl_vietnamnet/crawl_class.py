import io
import requests 
import bs4
import json
import time
import codecs
import os
import re
from urlparse import urljoin 

class crawl_vietnamenet(object):
    '''Crawl Viet Nam Net'''
    SOURCE_URL = ''
    TARGET_DIRECTORY = ''
    LIST_POST = []
    LIST_TITLE = []
    # methods
    
    def __init__(self, SOURCE_URL_ = 'http://vietnamnet.vn/vn/cong-nghe/'):
        '''Khoi tao class, cac bien co ban'''
        self.SOURCE_URL= SOURCE_URL_ 
        path = os.path.dirname(os.path.realpath(__file__))
        self.TARGET_DIRECTORY = path + '/results/'        
        if not os.path.exists(self.TARGET_DIRECTORY):
            os.makedirs(self.TARGET_DIRECTORY)

    def set_SOURCE_URL(self, SOURCE_URL_):
        self.SOURCE_URL=SOURCE_URL_

    def set_TARGET_DIRECTORY(self, TARGET_DIRECTORY_):
        self.TARGET_DIRECTORY = TARGET_DIRECTORY_   

    def get_content_post(self, CONTENT_URL):
        '''Crawl du lieu 1 bai viet'''
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

    def get_list_post(self):    
        '''Lay toan bo link bai viet trong duong dan'''
        r = requests.get(self.SOURCE_URL)
        if r.ok:
            s = bs4.BeautifulSoup(r.content, 'lxml')        
            list_obj = s.select('.item.clearfix.dotter > a')
            for obj in list_obj:           
                link_unjoin = obj.attrs['href'] # lay duong dan (thieu)
                link_obj = urljoin(self.SOURCE_URL, link_unjoin) # lay duong dan day du
                self.LIST_POST.append(link_obj)
                print(link_obj)            
        else: 
            print("khong truy cap duoc")
        

    def crawl_content_of_list_post(self):
        '''Crawl bai viet dua tren list link da co'''
        for link_post in self.LIST_POST:
            time.sleep(1)          
            data_to_json=self.get_content_post(link_post) # lay du lieu bai viet
            print(self.convert_json_create_file(data_to_json, self.get_file_name(link_post))) # tao file

    def get_list_link(self):
        '''Test function'''
        r = requests.get(self.SOURCE_URL)
        if r.ok:
            s = bs4.BeautifulSoup(r.content, 'lxml')        
            list_obj = s.select('.item.clearfix.dotter > a')
            for obj in list_obj:
                time.sleep(1)  
                link_unjoin = obj.attrs['href'] # lay duong dan (thieu)
                link_obj = urljoin(self.SOURCE_URL, link_unjoin) # lay duong dan day du
                print(link_obj)
                data_to_json=self.get_content_post(link_obj) # lay du lieu bai viet
                print(self.convert_json_create_file(data_to_json, self.get_file_name(link_unjoin))) # tao file
        else: 
            print("khong truy cap duoc")        


    def get_file_name(self, link_target):
        '''Tao duong dan File Name'''
        process_name_file_json = link_target.split("/")
        name_file_json = process_name_file_json[-1].split(".")
        file_name = self.TARGET_DIRECTORY + name_file_json[0] + '.json'
        return file_name

    def convert_json_create_file(self, json_data, file_name):
        '''Convert Json va tao file'''
        f = codecs.open(file_name, encoding='utf8', mode='w')
        json.dump(json_data, f, ensure_ascii=False, indent=2)
        return "done"

    def get_list_post_by_count(self, title='giao-duc', count=10):
        '''Lay bai viet dua tren so luong yeu cau'''
        URL_TARGET = "http://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={0}&p=1&s={1}".format(title,count)
        mk_js = requests.get(URL_TARGET)
        self.LIST_POST = re.findall('http://vietnamnet.vn(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', mk_js.content)
        return self.LIST_POST

    def get_list_title(self):
        '''Lay danh sach cac chu'''
        r = requests.get('http://vietnamnet.vn/')
        if r.ok:
            s = bs4.BeautifulSoup(r.content, 'lxml')        
            list_obj = s.select('.menu-top > li.item')
            for obj in list_obj:                 
                title_alias = obj.attrs['alias'] # lay duong dan (thieu)                
                self.LIST_TITLE.append(title_alias)
        else: 
            print("khong truy cap duoc")  
        return self.LIST_TITLE