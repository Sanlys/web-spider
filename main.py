import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse

rootURL = "https://www.youtube.com"
rootDomain = urlparse(rootURL).netloc

def urlNotExists(url):
		with open('urls.txt', 'r+') as f:
			if url not in f:
				return True

f = open('urls.txt', 'r+')

for url in f:
	try:
		r = requests.get(url)
		parsed = bs(r.text, "html.parser")
	except:
		continue

	#x = []

	file = open('urls.txt', 'a')
	for a in parsed.find_all('a', href=True):
		#x.append(a['href'])
		domain = urlparse(a['href']).netloc
		if(domain == rootDomain):
			file.write(a['href'] + '\n')

	#y = []
	#for i in x:
	#	if(i[0] == "/"):
	#		y.append(rootURL + i)
	#	else:
		#y.append(i)	


	#file = open('urls.txt', 'a')

	#for i in y:
		#if(urlNotExists(i)):
			#file.write(i)
			#print(i)
