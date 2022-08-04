import json
import re
import requests

def find_shortened_links_in_post(posts, shortener_provider):
	urls = []
	for post in posts:
		# Find text starting with shortener_provider and stop at a not word character
		for url in re.findall(shortener_provider + "(.*?)\W", post['post_content']):
			urls.append(url)
	return list(dict.fromkeys(urls))

def loop_through_shortened_links(urls, shortener_provider):
	# Header to access websites that requires it
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
	for url in urls:
		url_short = shortener_provider + url
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
				# Print redirections
				print('From: ' + url + ' - To ' + redirect.url + '\n')

file = open('export.json')
posts = json.load(file)

urls_bit_ly = find_shortened_links_in_post(posts, 'https://bit.ly/')
urls_tiny = find_shortened_links_in_post(posts, 'https://tinyurl.com/')

# Turn array into dict to delete duplicates	
loop_through_shortened_links(urls_bit_ly, 'https://bit.ly/')
loop_through_shortened_links(urls_tiny, 'https://tinyurl.com/')

file.close()
