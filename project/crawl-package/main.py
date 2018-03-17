# import
import crawl_vietnamnet as lib
from crawl_vietnamnet import crawl_class
import os 

# main component

crawl_a=crawl_class.crawl_vietnamenet()

def example_1():
    """basic"""
    crawl_a.get_list_post()
    crawl_a.crawl_content_of_list_post()

def example_2():
    """Lay theo so luong""" 
    print(crawl_a.get_list_post_by_count(title='giao-duc',count=20))
    crawl_a.crawl_content_of_list_post()
def example_3():
    """crawl 1 link xac dinh"""
    crawl_a.LIST_POST.append('http://vietnamnet.vn/vn/cong-nghe/mua-galaxy-s9-s9-tiet-kiem-den-9-trieu-dong-434449.html')
    crawl_a.crawl_content_of_list_post()    
def example_4():
    """Lay list title"""
    print(crawl_a.get_list_title())

def example_5():
    """Thu muc nhan ket qua"""
    print(crawl_a.TARGET_DIRECTORY)

def main():        
    #example_5()  
    #example_4()  
    #example_3()
    example_2()

if __name__ == "__main__":
    main()