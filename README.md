# youtube-playlist-scraper
downloading playlist on channels from youtube, seperate directory. 

<h4>:))) => Already Exits from https://github.com/rg3/youtube-dl/blob/master/README.md#readme :</h4>

<p>Download YouTube playlist videos in separate directory indexed by video order in a playlist</p>
$ youtube-dl -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re

<p>Download all playlists of YouTube channel/user keeping each playlist in separate directory:</p>
$ youtube-dl -o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/user/TheLinuxFoundation/playlists

# Installing
```
  $ pip install requests bs4 youtube-dl   #installing moduls
  $ git clone https://github.com/pleycpl/youtube-playlist-scraper
```
# Usage
```
  $ cd youtube-playlist-scraper
  $ vim main.py  #changed url
  $ python main.py
```
