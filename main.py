import yt_dlp

link = input("Enter YT video link to dwnload:")
options = {
    'format':'best',        # Quality
    'outtmpl':'download.mp4'  #filename
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([link])

print("Finished Downloading......!!!")