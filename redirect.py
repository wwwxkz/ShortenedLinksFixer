import json
import re
import requests

f = open('export.json')
data = json.load(f)

def loop_through_urls_found(urls, url_provider_base):
    url_logger = []
    for url in urls:
        url = url_provider_base + url
        # Do not show duplicates 
        for url_log in url_logger:
            if(url_log == url):
                url = ''
        # Checks for empty url
        if(url != ''):
            # Go to link and save redirection
            redirect = requests.get(url)
            print('From: ' + url + ' - To ' + redirect.url + '\n')
            url_logger.append(url)

for i in data:
    # Regex based in my use
    url_bit_ly = re.findall("https://bit.ly/(.*?)\W", i['post_content'])
    url_tiny = re.findall("https://tinyurl.com/(.*?)\W", i['post_content'])
    loop_through_urls_found(url_bit_ly, 'https://bit.ly/')
    loop_through_urls_found(url_tiny, 'https://tinyurl.com/')

f.close()
