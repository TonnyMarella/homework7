from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=C6S3dMt1s_M&list=WL&index=7&t=7s')

# print(yt.streams.filter(file_extension='mp4'))
stream = yt.streams.get_by_itag(22)
stream.download()