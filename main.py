import requests
from bs4 import BeautifulSoup as bs

rootURL = "https://www.youtube.com"

def urlNotExists(url):
		with open('urls.txt', 'r+') as f:
			if url not in f:
				return True

f = open('urls.txt', 'r+')

for url in f:
	try:
		r = requests.get(url)
	except:
		continue
	if(r.status_code == 200):
		parsed = bs(r.text, features="lxml")
	else:
		continue

	x = []

	for a in parsed.find_all('a', href=True):
		x.append(a['href'])
	y = []
	for i in x:
	#	if(i[0] == "/"):
	#		y.append(rootURL + i)
	#	else:
		y.append(i)	


	file = open('urls.txt', 'a')

	for i in y:
		temp = (i + '\n')
		if(urlNotExists(temp)):
			file.write(temp)
			print(temp)
