import ffmpeg
input = ffmpeg.input('https://ma7moud3ly.github.io/video.mp4')
crop=input.crop(x=0,y=0,width=200,height=200)
ffmpeg.run(ffmpeg.output(crop, 'crop.mp4'))