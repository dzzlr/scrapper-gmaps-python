import json

from scrapper.mongodb_config import MongoDBConfig
from scrapper.webdriver_config import WebDriver

from scrapper.utils import process_date

if __name__ == '__main__':
    f = open('metadata.json')
    metadata = json.load(f)
    datas = metadata['data']
    f.close()
    
    for data in datas:
        if data['status'] == True:
            location = data['name']
            location_url = data['url']
            reviews_count = data['reviews_count']
            
            loop_optimizer = 120 if reviews_count > 1000 else abs(int(reviews_count // 10) - 1)
            wd = WebDriver("C:\\edgedriver_win64\\msedgedriver.exe")
            wd.scrape(location, location_url, loop_optimizer)
            
        time.sleep(3)
