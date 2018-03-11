# import
import requests 
import bs4
import json
import time
import html5lib

from urlparse import urljoin #urljoin
#from urllib.parse import urljoin

SOURCE_URL = 'http://vietnamnet.vn/vn/cong-nghe/'
# function

def get_content_post(CONTENT_URL):
    data = {}
    r = requests.get(CONTENT_URL)
    if r.ok:
        s = bs4.BeautifulSoup(r.content.decode('utf-8','ignore'), 'html5lib')        
        title = s.select_one('h1.title').next
        data['title'] = title 
        content = s.select_one('#ArticleContent')
        data['content'] = content
        time = s.select_one('.ArticleDate').next
        data['time'] = time 
        
    else: 
        print("khong truy cap duoc")
    return data 

def get_list_link():
    list_post = []
    r = requests.get(SOURCE_URL)
    if r.ok:
        s = bs4.BeautifulSoup(r.content, 'lxml')        
        list_obj = s.select('.item.clearfix.dotter > a')
        for obj in list_obj:
            time.sleep(1)
            #print(obj.attrs['href'])
            #print(urljoin(SOURCE_URL, obj.attrs['href']))
            link_obj = urljoin(SOURCE_URL, obj.attrs['href'])
            print(link_obj)
            # list_post.append(get_content_post(link_obj))
            #r = json.dumps(get_content_post(link_obj))
            
            print("done")
            #print(r)
    else: 
        print("khong truy cap duoc")

    return list_post
# main
def main():
    #print(get_list_link())
    print(get_content_post('http://vietnamnet.vn/vn/cong-nghe/tin-cong-nghe/samsung-dang-nam-giu-cong-nghe-sac-pin-dot-pha-434821.html'))


if __name__ == "__main__":
    main()