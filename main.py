import requests
from bs4 import BeautifulSoup

youtube = "https://www.youtube.com"
# The New Boston channel
url = "https://www.youtube.com/user/thenewboston/playlists"
print("Channel url : " + url)

response = requests.get(url)
html = response.content # All source code of the web page
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

ul = soup.findAll('ul', attrs={'id': 'channels-browse-content-grid'})
print(ul)
