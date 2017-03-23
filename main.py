import requests
from bs4 import BeautifulSoup
import subprocess
import youtube_dl
import os
import sys
from selenium import webdriver

def getSourceCodeWithSelenium(url):
    """
        Getting Source Code on Website with Selenium, because javascript
    """
    print("Channel url: " + url)
    driver = webdriver.Firefox()
    driver.get(url)
    button = driver.find_element_by_css_selector('.yt-uix-load-more')
    print(button)
    button.click();
    sourceCode = driver.page_source
    print("[+] Getting Source Code is Done, in Selenium")
    return sourceCode

def getSourceCode(url):
    """ - Getting Source Code on Website
        http://stackoverflow.com/questions/17011357/what-is-the-difference-between-content-and-text#17011420
        r.text is the content of the response in unicode
        r.content is the content of the response in bytes.
    """
    print("Channel url: " + url)
    sourceCode = requests.get(url).content
    print("[+] Getting Source Code is Done")
    return sourceCode

def getPlaylistData(sourceCode):
    """ - Getting Data like Playlist Name and Link """
    soup = BeautifulSoup(sourceCode, 'html.parser')
    #<a class="yt-uix-sessionlink yt-uix-tile-link  spf-link  yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr" title="ECMAScript 6 / ES6 New Features Tutorials" aria-describedby="description-id-514268" data-sessionlink="ei=uHmSWOS8LM6p1gK7-a2oBg&amp;ved=CDgQlx4iEwjk-MvOkPDRAhXOlFUKHbt8C2Uomxw" href="/playlist?list=PL6gx4Cwl9DGBhgcpA8eTYYWg7im72LgLt">ECMAScript 6 / ES6 New Features Tutorials</a>
    playlist = {}
    playlistName = ""
    playlistLink = ""
    for a in soup.findAll('a', attrs={'class':'yt-uix-tile-link'}):
        playlistName = a.get('title')
        playlistName = playlistName.replace(" ", "") # Deleting space
        playlistName = playlistName.replace("/", "_") # Change path seperator
        playlistLink = a.get('href')
        playlist[playlistName] = playlistLink

    print("[+] Getting Playlist Name and Link is Done")
    return playlist

def displayPlaylist(playlist):
    for name in playlist:
        print("Name : {} , Link :{} ".format(name, playlist[name]))


def creatDirectory(playlist, youtube):
    """ First creating directory, then dowloading playlist each directory """
    for name in playlist:
        # Creatin directory
        directoryName = "./"
        directoryName += name
        try:
            # https://pymotw.com/2/subprocess/
            subprocess.check_call("mkdir " + directoryName, shell=True)
        except subprocess.CalledProcessError as e:
            print(e.output)
            continue
        # Downloading Playlist
        link = youtube + playlist[name]
        options = {
            'outtmpl' : directoryName + '/%(title)s-%(id)s.%(ext)s'
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([link])

def main():
    # Downloading all playlists each directory from TheNewBoston channel
    youtube = "https://www.youtube.com"
    url = sys.argv[1]
    sourceCode  = getSourceCodeWithSelenium(url)
    playlist    = getPlaylistData(sourceCode)
    displayPlaylist(playlist)
    creatDirectory(playlist, youtube)

if __name__ == "__main__":
    main()



"""
ul = soup.find('ul', attrs={'id': 'channels-browse-content-grid'})
# print(ul)  <ul id="channels-browse-content-grid"></ul>

playlist = {}    # Creating Dictionary
playlist_name = ""
playlist_link = ""
for li in ul.findAll('li', attrs={'class': 'channels-content-item yt-shelf-grid-item'}):
    # print(li.prettify())
    for a in li.findAll('a', attrs={'class': 'yt-uix-tile-link'}): # Playlist-name
        # print(a.prettify())
        # print(a.get('title'))
        playlist_name = a.get('title')
        playlist_name = playlist_name.replace(" ", "") # Cleaning space
    for a in li.findAll('a', attrs={'class': 'yt-pl-thumb-link'}): # Playlist-link
        # print(a.prettify())
        # print(a.get('href'))
        playlist_link = a.get('href')
    playlist[playlist_name] = playlist_link

for name in playlist:
    # First creating directory, then dowloading playlist each directory
    link = youtube + playlist[name]
    directory_name = "./"
    directory_name += name
    subprocess.call("mkdir " + directory_name, shell=True)
    # Downloading Playlist
    options = {
        'outtmpl' : directory_name + '/%(title)s-%(id)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([link])

# if you want download metadata use that code
options = {}

with youtube_dl.YoutubeDL(options) as ydl:
    metadata = ydl.extract_info(link)

print("Uploader : {}\nViews : {}".format(
    metadata['uploader'], metadata['view_count']))

"""
