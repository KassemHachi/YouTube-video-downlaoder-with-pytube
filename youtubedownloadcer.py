from pytube import YouTube
from pytube import YouTube
from pytube.cli import on_progress 
link=input('Put your Youtube url : ')
print("Please Wait while we preparing the video ... ")
yt=YouTube(link,on_progress_callback=on_progress)
videos=yt.streams.get_highest_resolution()
videos.download()
print(" ")
print("Your video is ready to play .")