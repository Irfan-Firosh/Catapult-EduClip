from moviepy.editor import *
from testSentences import *
from videoOperations import *
import os

def clipper(file_name, id, question):
    os.environ['IMAGEIO_FFMPEG_EXE'] = 'ffmpeg'
    val = find_seg(id, question)
    clip = VideoFileClip(filename=file_name)
    value = clip.end
    print(val)
    start = val[0][0]["start"]
    end = start + 30
    if (end > value):
        end = value
    clip = VideoFileClip(file_name).subclip(start,end)
    clip.write_videofile("metadata/extracted/output.mp4")
    return "metadata/extracted/output.mp4"

