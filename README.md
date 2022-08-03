# linkShortenedFixer

Plugin created to fix shortened links with bit.ly and tinyurl, the providers of the service can be changed the in the code, and if it keeps the pattern of base/hash-to-your-page it will work

Explaining my use, I used the Wordpress plugin Search Regex with these 2 regular expressions

```https://bit.ly/(.*?)\W```
```https://tinyurl.com/(.*?)\W```

Exported the results in a json file with this format

```
[
	{"ID":"","post_title":"","post_name":"","post_type":"","post_content":""},
	{"ID":"","post_title":"","post_name":"","post_type":"","post_content":""}
]
```

and ran the code with

``` python3 redirect.py > output.txt ```

I did some other filters in this output.txt and asked for my coworkers verify

then I used the same plugin and replaced the shortened links with the direct link as it was not necessary for us anymore

if there is a images/ folder in your redirected url, the plugin will try to download the url and save with the name that comes after images/, it will keep the file extension .pdf, .docx, .png, so on
