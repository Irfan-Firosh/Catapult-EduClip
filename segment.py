from youtube_transcript_api import YouTubeTranscriptApi
import json
import os
import math

transcript_path = "metadata/transcripts"

def get_Transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    path = f'{transcript_path}/transcript.json'
    with open(path, "w") as file:
        json.dump(transcript, file, indent=4) 

def clearDir():
    path = f'metadata/transcripts/'
    for vid in os.listdir(path):
        path = os.path.join(path, vid)
        os.remove(path)

# Returns a dict = {"key": beginning segment, "item": ending segment}
def segmentFile(duration: int):
    assert(0<duration and duration<=60)
    ret = []
    path = f'{transcript_path}/transcript.json'
    with open(path, 'r') as file:
        json_data = json.load(file)
    last = json_data[-1]
    vid_length = last["start"] + last["duration"]
    segments = int(math.ceil(vid_length/duration))
    ret.append(json_data[0])
    for i in range(0,segments):
        start = (i/(segments)) * vid_length
        for item in json_data:
            error = abs(item["start"]- start)/item["start"]
            if error <= 0.05:
                #print(item)
                ret.append(item)
    return ret

def completeExtract(duration: int):
    path = f'{transcript_path}/transcript.json'
    with open(path, 'r') as file:
        json_data = json.load(file)
    segments = segmentFile(duration)
    ret = []
    ends = []
    starts = []
    for item in segments:
        starts.append(item["start"])
    for index, item in enumerate(json_data):
        if (item["start"] in starts):
            ends.append(index)
    i = 0
    for end in ends[1:]:
        ret.append([segments[i], json_data[end - 1]])
        i = i + 1
    ret.append([segments[-1], json_data[-1]])
    return ret

def getText(start, end):
    result = ""
    found_beginning = False
    path = f'{transcript_path}/transcript.json'
    with open(path, 'r') as file:
        json_data = json.load(file)
    for item in json_data:
        if item["start"] == start:
            found_beginning = True
        if found_beginning:
            result += item["text"] + " "
        if item["start"] == end:
            break
    return result

def getSegment(id, duration: int):
    clearDir()
    get_Transcript(id)
    ret = completeExtract(duration)
    textSeg = []
    for item in ret:
        str = " "
        str = getText(item[0]["start"], item[1]["start"])
        textSeg.append(str)
    return ret, textSeg
