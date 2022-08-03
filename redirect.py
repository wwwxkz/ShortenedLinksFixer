import json
import re
import requests

f = open('export.json')
data = json.load(f)

def loop_through_urls_found(urls, url_provider_base):
    # Header to access websites that requires it
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
    # Log past url cases, if it appears again, do nothing
    url_logger = []
    for url in urls:
        url_short = url_provider_base + url
        # Do not show duplicates 
        for url_log in url_logger:
            if(url_log == url):
                url_short = ''
        # Checks for empty url
        if(url_short != ''):
            redirect = requests.get(url_short, allow_redirects=True, headers=headers)
            # If it is in CMS images/ folder download it
            if ('images' in redirect.url):
                with open(redirect.url.split('images/')[1], 'wb') as blob:
                    # For bigger filles it would be better increasing chunk size
                    for chunk in redirect.iter_content(1024):
                        blob.write(chunk)
            else:
                # Print redirections end
                print('From: ' + url + ' - To ' + redirect.url + '\n')
                url_logger.append(url)

for i in data:
    # Regex based in my use
    url_bit_ly = re.findall("https://bit.ly/(.*?)\W", i['post_content'])
    url_tiny = re.findall("https://tinyurl.com/(.*?)\W", i['post_content'])
    loop_through_urls_found(url_bit_ly, 'https://bit.ly/')
    loop_through_urls_found(url_tiny, 'https://tinyurl.com/')

f.close()
