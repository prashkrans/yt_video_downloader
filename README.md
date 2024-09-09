# Youtube Video Downloader
- A Python gradio app that downloads YouTube videos given their URL.
- It also provides an option to download only the audio track for the given video URL.

### Demo Video:
https://github.com/user-attachments/assets/b5ba3a77-83d5-4a8a-939f-c914dee08665

### Pre-requisites:
FFMPEG:
`sudo apt install ffmpeg`

### Setup:
- Clone the repo and move to the root dir.
- Create a python virtual environment.
- Install the requirements.
- Ignore the dependency conflict between gradio and yt-dlp
- Run main_gradio.py

### Note:
- Replaced pytube with yt-dlp (which is a fork of youtube-dl but better)
- Simply install the requirements as the versions mentioned, it'd work fine