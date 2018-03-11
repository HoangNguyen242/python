import json
import io

r = {'is_claimed': 'True', 'rating': 3.5}
#r = json.dumps(r)

#loaded_r = json.loads(r)
#loaded_r['rating'] #Output 3.5
#type(r) #Output str
#type(loaded_r) #Output dict

with open('/root/Python/Crawl-python/data.json', 'w') as outfile:  
    json.dump(r, outfile)
