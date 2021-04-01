from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

'''program to extract short video sequence from a large video file'''

videoName = "Home/inputpath/namevideo.mp4"
start_time = 103
end_time = 132

ffmpeg_extract_subclip(videoName, start_time, end_time, targetname="Home/ouputpath/namevideo.mp4")
