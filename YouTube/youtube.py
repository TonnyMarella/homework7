from pytube import YouTube

yt = YouTube('https://youtu.be/X_b1bDTVkBQ')

# print(yt.streams.filter(file_extension='mp4'))
stream = yt.streams.get_by_itag(22)
stream.download()