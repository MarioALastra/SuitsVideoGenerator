import os

c_dir = os.chdir("Output")
c_dir = os.listdir()

video_title = " - Suits Absolute Power OST"

for x in c_dir:
    mp4_removed = x[:-len(".mp4")]
    final_title = mp4_removed + video_title + ".mp4"
    print(final_title)
    os.rename(x,final_title)


