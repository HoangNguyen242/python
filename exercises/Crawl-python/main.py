# import
import requests 
import bs4
from urllib.parse import urljoin

SOURCE_URL = 'http://vietnamnet.vn/vn/cong-nghe/'
# function

def get_content_post(CONTENT_URL):
    pass

def get_list_link():
    r = requests.get(SOURCE_URL)
    if r.ok:
        s = bs4.BeautifulSoup(r.content, 'lxml')        
        list_obj = s.select('.item.clearfix.dotter > a')
        for obj in list_obj:
            #print(obj.attrs['href'])
            print(urljoin(SOURCE_URL, obj.attrs['href']))
    else: 
        print("khong truy cap duoc")

# main
def main():
    #get_list_title()
    get_list_link()

if __name__ == "__main__":
    main()