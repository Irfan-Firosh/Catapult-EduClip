from youtubesearchpython import VideosSearch
from pytube import YouTube
from pytube.cli import on_progress
import json
import os


# Search for videos that align with the prompt and then outputs them
def search_videos(prompt):
    videos = VideosSearch(prompt, limit=5)
    with open("metadata/videoInfo.json", "w") as file:
        json.dump(videos.result(), file, indent=4)

# Retrieves the id and name of yt video,
# returns a dict with key = id, and value = title
def get_info():
    return_dict = {}
    with open("metadata/videoInfo.json", "r") as file:
        data = json.load(file)
        for video in data["result"]:
            return_dict[video["id"]] = video["title"]
    return return_dict

# downloads chosen id
def downloadID(Title, yt_dict):
    for id in yt_dict:
        if yt_dict[id] == Title:
            download_yt(id)

# Clears download directory
def clear_downloads():
    dpath = f'metadata/downloaded/'
    for vid in os.listdir(dpath):
        path = os.path.join(dpath, vid)
        os.remove(path)

def get_video_path():
    dpath = f'metadata/downloaded/'
    for vid in os.listdir(dpath):
        path = os.path.join(dpath, vid)
        return path

# Downloads desired yt videos
def download_yt(id):
    try:
        url = f'http://youtube.com/watch?v={id}'
        dpath = f'metadata/downloaded/'
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(progressive = True, file_extension = "mp4").first()
        stream.download(dpath)
    except Exception as e:
        print("Failed in dowloading...", e)

def main(query):
    search_videos(query)
    yt_dict = get_info()
    return yt_dict