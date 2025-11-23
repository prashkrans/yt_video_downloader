# Youtube Video Downloader
- A Python gradio app that downloads YouTube videos given their URL.
- It also provides an option to download only the audio track for the given video URL.

### Demo Video:
https://github.com/user-attachments/assets/b5ba3a77-83d5-4a8a-939f-c914dee08665

### Pre-requisites:
**FFMPEG:**  
a. Linux (Debian 13.0): `sudo apt install ffmpeg`  
b. MacOS (Tahoe 26.1)  
1. Install Brew: 
   1. Open terminal and paste: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
   2. Provide sudo password and wait for the installation to finish.
   3. Next steps: Run these commands in your terminal to add Homebrew to your PATH:
   ```
    echo >> /Users/mac_m4/.zprofile
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/mac_m4/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
   ```
   4. Run `brew help` to get started

2. Use brew to install ffmpeg:`brew install ffmpeg`  
Verify ffmpeg version:  
a. Linux (Debian 13.0): `ffmpeg --version`  
b. MacOS (Tahoe 26.1): `ffmpeg -version`

3. For MacOS (Tahoe 26.1) only: 
   1. `nano ~/.zshrc`
   2. Add the line `export PATH="/opt/homebrew/bin:$PATH"`, save and exit
   3. `source ~/.zshrc`

### Setup:
- Clone the repo and move to the root dir.
- Create a python virtual environment.
- Install the requirements.
- Ignore the dependency conflict between gradio and yt-dlp
- Run main_gradio.py

### Quick setup for Windows 10/11:
- Install [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)
- Run the `YT_Video_Downloader_Setup.bat` (only the first time) inside the docker directory by double clicking on it.
- It automatically pulls a working image (~500 MBs) from the public repo of `yt_video_downloader` from the docker hub, then creates a container from it and runs it.
- There's no need to clone the repo here as the `.bat` file and the `docker image` from the docker hub does everything here.
- Then use the docker desktop console to stop and start this container as required.
- **Troubleshoot:** Whenever there's any issue simply delete both the yt_video_downloader container and image in the docker desktop console and re-run the `YT_Video_Downloader_Setup.bat` (only once).

### Note:
- Replaced pytube with yt-dlp (which is a fork of youtube-dl but better)
- Simply install the requirements as the versions mentioned, it'd work fine
- Error: Sign in to confirm you’re not a bot. This helps protect our community. Learn more. Fix: Simply update yt-dlp version.
