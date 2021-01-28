from moviepy.editor import *
import os

def MakeVideo(audio_file, video_title):
    image = ImageClip("..\..\Resources\main.png")
    audio = AudioFileClip(audio_file)
    video_length = audio.duration

    final_title = audio_file[:-len(".wav")]
    print(final_title)

    image.set_audio(audio).set_duration(video_length).write_videofile("../../Output/{}.mp4".format(final_title), fps = 1)


#   Initzalize Folders
c_dir = os.listdir()

os.chdir("Resources/Music")

c_dir = os.listdir()

video_title = " - Suits: Absolute Power OST"

for x in c_dir:
    MakeVideo(x, video_title)

