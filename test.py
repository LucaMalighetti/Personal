import yt_dlp

playlist_url = 'https://www.youtube.com/watch?v=e_oFiNyOgiw&list=PLvC0GZWIwKUfGWspoJ1rkyBN8xjrobTwI'

ydl_opts={
    'format':'best',
    'outtmpl':"%(playlist_title)s/%(title)s.%(ext)s",
    'quiet':False
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])