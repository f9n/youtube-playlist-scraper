import requests

youtube = "https://www.youtube.com"
# The New Boston channel
url = "https://www.youtube.com/user/thenewboston/playlists"
print("Channel url : " + url)

response = requests.get(url)
html = response.content # All source code of the web page

print(html)
