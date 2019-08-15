from bs4 import BeautifulSoup
import requests,os,sys,re

# Scrape urls usage : scrape.py <target>

print(len(sys.argv))
if len(sys.argv) < 2:
	target =  "https://www.programcreek.com/python/example/84097/cv2.circle"
else:
	target = sys.argv[1]

def ScrapeLinks(victim):
	url = raw_input(victim)
	r  = requests.get("http://" + url, timeout=5)
	data = r.text
	soup = BeautifulSoup(data)
	for link in soup.find_all('a'):
		print(link.get('href'))

def S(victim):
	page_response = requests.get(victim, timeout=5)
	soup = BeautifulSoup(page_response.content, "html.parser")
	textContent = []
	for i in range(0, 20):
	    paragraphs = soup.find_all("pre", attrs={"class":"prettyprint"})[i].text
	    textContent.append(paragraphs)
	return textContent


def BoilSoup(victim):
	page_response = requests.get(victim, timeout=5)
	soup = BeautifulSoup(page_response.content, "html.parser")
	
	i=1
	# for blobje in soup.find_all("pre", attrs={"class":"prettyprint"})[i].text:
	for blobje in soup.findAll('pre', attrs={"class":"prettyprint"}):
		# print(blobje)
		# os.system('echo "' + str(blobje).replace('<pre class=prettyprint>','').replace('<pre>','') + '" >> opencv_examples/cv2_example_' + str(i) + '.py')
		blob = re.sub('<[^<]+?>', '', str(blobje))
		os.system('echo "' + str(blob) + '" >> opencv_examples/cv2_example_' + str(i) + '.py')
		i += 1


# print(S(target))
BoilSoup(target)

