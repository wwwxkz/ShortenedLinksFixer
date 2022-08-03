import json
import re
import requests

f = open('export.json')
data = json.load(f)

for i in data:
    url_bit_ly = re.findall("https://bit.ly/(.*?)\W", i['post_content'])
    url_tiny = re.findall("https://tinyurl.com/(.*?)\W", i['post_content'])
    for url in url_bit_ly:
        if(url != ''):
            url = 'https://bit.ly/' + url
            redirect = requests.get(url)
            print('From: ' + url + ' - To: ' + redirect.url + '\n')
    for url in url_tiny:
        if(url != '' and url != 'associe'):
            url = 'https://tinyurl.com/' + url
            redirect = requests.get(url)
            print('From: ' + url + ' - To: ' + redirect.url + '\n')

f.close()
