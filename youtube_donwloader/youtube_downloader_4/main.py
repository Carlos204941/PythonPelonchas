# Projet "Youtube Downloader"

# module : pytube

from pytube import YouTube

# url = "https://www.youtube.com/watch?v=9bZkp7q19f0"

BASE_YOUTUBE_URL = "https://www.youtube.com"

while True:
    url = input("Donnez l'url de la vidéo Youtube à télécharger: ")
    #if url[:len(BASE_YOUTUBE_URL)] == BASE_YOUTUBE_URL:
    if url.lower().startswith(BASE_YOUTUBE_URL):
        break
    print("ERREUR : Vous devez rentrer une URL de video Youtube")



# vérifier que l'url commence par "https://www.youtube.com"
# si ce n'est pas le cas 
# - afficher une erreur
# - reposer la question

def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize

    print(f"Progression du téléchargement {int(percent)}%")



youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)

print("TITRE: " + youtube_video.title)
print("NB VUES:", youtube_video.views)

print("STREAMS")
for stream in youtube_video.streams.fmt_streams:
    print("  ", stream)

# stream = youtube_video.streams.get_by_itag(18)
stream = youtube_video.streams.get_highest_resolution()
print("Steam vidéo: ", stream)
print("Téléchargement...")
stream.download()
print("OK")
