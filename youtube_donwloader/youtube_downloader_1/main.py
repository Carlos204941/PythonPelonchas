# Projet "Youtube Downloader"

# module : pytube

from pytube import YouTube

url = "https://www.youtube.com/watch?v=9bZkp7q19f0"

youtube_video = YouTube(url)
print("TITRE: " + youtube_video.title)
print("NB VUES:", youtube_video.views)
