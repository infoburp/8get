import urllib.request, urllib.parse, urllib.error, os, re, glob
url = input('Enter base url, e.g. https://8chan.co/b/res/527104.html (or return to use google.com)')
if url == '':
	url = 'http://google.com'
i=1
match = []
try:
	urllib.request.urlretrieve(url,'base.html')
	print(url)
except urllib.error.HTTPError as err:
	print(err.code)
with open('base.html') as html:
    content = html.read()
    matches = re.findall(r'\ssrc="([^"]+)"', content)
for match in matches:
	if match.find(".js") == -1:
		if match.find(".php") == -1:  
			try:
				split = urllib.parse.urlsplit('8chan.co'+match)
				filename = split.path.split("/")[-1]
				urllib.request.urlretrieve('http://8chan.co'+match, filename)
				print(url+match)
			except urllib.error.HTTPError as err:
				print(err.code)
