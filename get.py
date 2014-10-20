import urllib.request, urllib.parse, urllib.error, os, re
url = raw_input('Enter base url, e.g. https://8chan.co/b/res/527104.html')
	try:
		urllib.request.urlretrieve(url,'base.html')
		print(url)
	except urllib.error.HTTPError as err:
		print(err.code)
with open('base.html') as html:
    content = html.read()
    matches = re.findall(r'\ssrc="([^"]+)"', text)
    matches = ' '.join(matches)
print(matches)
