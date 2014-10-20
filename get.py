import urllib.request, urllib.parse, urllib.error, os, re, glob
board = input('Enter board e.g. "b":')
if board=='':
	board='b'
thread = input('Enter thread e.g. "527104":')
if thread=='':
	thread='527104'
thumbs = input('Download thumbs(return), or full(y, or anything else):')
url='https://8chan.co/'+board+'/res/'+thread+'.html'
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
			if thumbs == '':
				try:
					split = urllib.parse.urlsplit('8chan.co'+match)
					filename = split.path.split("/")[-1]
					urllib.request.urlretrieve('http://8chan.co'+match, filename)
					print(url+match)
				except urllib.error.HTTPError as err:
					print(err.code)
			if thumbs != '':
				try:
					split = urllib.parse.urlsplit('8chan.co'+match.replace("thumb","src"))
					filename = split.path.split("/")[-1]
					urllib.request.urlretrieve('http://8chan.co'+match.replace("thumb","src"), filename)
					print(url+match.replace("thumb","src"))
				except urllib.error.HTTPError as err:
					print(err.code)
