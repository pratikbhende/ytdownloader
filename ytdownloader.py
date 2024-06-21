import pytube	
link = input('Paste the url here : ')
video = pytube.YouTube(link)
video.streams.first().download()

print("Download Successfully, ",link)
