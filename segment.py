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
    print(vid_length)
    segments = int(math.ceil(vid_length/duration))
    print(segments)
    ret.append(json_data[0])
    for i in range(0,segments):
        start = (i/(segments)) * vid_length
        print(start)
        for item in json_data:
            error = abs(item["start"]- start)/item["start"]
            if error <= 0.05:
                #print(item)
                ret.append(item)
    print(ret)
    print(len(ret))
    return ret

def completeExtract(duration: int):
    path = f'{transcript_path}/transcript.json'
    with open(path, 'r') as file:
        json_data = json.load(file)
    ret = []
    segments = segmentFile(duration)
    for item in segments[:-1]:
        temp = []
        temp.append(item)
        for i, json in enumerate(json_data):
            if item["start"] == json["start"]:
                temp.append(json_data[i-1])
        ret.append(temp)
    ret.append([segments[-1], json_data[-1]])
    

clearDir()
get_Transcript("yvTZwGQYHww")
completeExtract(60)