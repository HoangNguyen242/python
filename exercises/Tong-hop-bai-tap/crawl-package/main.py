# import
import crawl_vietnamnet as lib
from crawl_vietnamnet import crawl_class
import os 

# main component
def main():    
    crawl_a=crawl_class.crawl_vietnamenet()
    print(crawl_a.TARGET_DIRECTORY)
    crawl_a.get_list_post()
    crawl_a.crawl_content_of_list_post()
    #crawl_a.LIST_POST.append('http://vietnamnet.vn/vn/cong-nghe/mua-galaxy-s9-s9-tiet-kiem-den-9-trieu-dong-434449.html')

    #print(crawl_a.LIST_POST)
    #crawl_a.get_file_name('http://vietnamnet.vn/vn/cong-nghe/mua-galaxy-s9-s9-tiet-kiem-den-9-trieu-dong-434449.html')
    #crawl_a.crawl_content_of_list_post()

if __name__ == "__main__":
    main()