import re

import moviepy.editor as mp
import requests
from fastapi import FastAPI
from ShazamAPI import Shazam
import uvicorn

app = FastAPI()


@app.get("/download")
async def download(url: str):
    with open('video.mp4', 'wb') as f:
        response = requests.get(url, allow_redirects=False)
        video_id = re.search(r'tiktok\.com\/@.*\/video\/([0-9]+)\?', response.headers['Location']).group(1)
        f.write(requests.get(f'https://www.tikwm.com/video/media/hdplay/{video_id}.mp4').content)
    with mp.VideoFileClip("video.mp4") as video:
        video.audio.write_audiofile("audio.mp3")
    recognize_generator = Shazam(open('audio.mp3', 'rb').read()).recognizeSong()
    matches = set()
    for match in recognize_generator:
        print(match[1].keys())
        if "track" in match[1].keys():
            matches.add(f'{match[1]["track"]["subtitle"]} ❖ {match[1]["track"]["title"]}')
    return matches

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=4727)
