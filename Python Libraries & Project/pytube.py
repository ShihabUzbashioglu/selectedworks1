from pytube import Youtube


#url

video_url = ""

#init

yt = Youtube(video_url)

#select resoulution

stream = yt.streams.get_highest_resolution()

#download 
stream.download()