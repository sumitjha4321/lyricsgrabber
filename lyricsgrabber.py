import requests
from bs4 import BeautifulSoup
import urllib


song_name = raw_input("Enter the name of the song: ")
print "Searching for",song_name,"...\n\n"
data = {'q': song_name}
url = "http://search.azlyrics.com/search.php?" + urllib.urlencode(data)




headers = { 'Accept':'*/*',
			'Accept-Encoding':'gzip, deflate, sdch',
			'Accept-Language':'en-US,en;q=0.8',
			'Cache-Control':'max-age=0',
			'Connection':'keep-alive',
			'Proxy-Authorization':'Basic ZWRjZ3Vlc3Q6ZWRjZ3Vlc3Q=',
			'If-Modified-Since':'Fri, 13 Nov 2015 17:47:23 GMT',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
			}

r = requests.get(url, proxies=proxies, headers=headers)
soup = BeautifulSoup(r.content)

links = soup.find_all("table", {"class":"table table-condensed"})

if len(links) == int(2):
	
	links = links[1].find_all("td", {"class":"text-left visitedlyr"})
else:
	
	links = soup.find_all("td", {"class":"text-left visitedlyr"})

counter = 0
for link in links:
	counter +=1
	print counter,".", link.contents[1].text, "by", link.contents[3].text
	
choice = raw_input("\n\nEnter Choice: ")


if int(choice) == int(1):
	html = str(links[0]).split('<a href="')
	link = str(html[1]).split('"')[0]

elif int(choice) == int(2):
	html = str(links[1]).split('<a href="')
	link = str(html[1]).split('"')[0]

elif int(choice) == int(3):
	html = str(links[2]).split('<a href="')
	link = str(html[1]).split('"')[0]


elif int(choice) == int(4):
	html = str(links[3]).split('<a href="')
	link = str(html[1]).split('"')[0]


else:
	html = str(links[4]).split('<a href="')
	link = str(html[1]).split('"')[0]
	
r = requests.get(link, proxies=proxies, headers=headers)

print ((r.content).split("<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->"))[1].split("</div")[0].replace("<br>", "")
